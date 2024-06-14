from models import init_db, Teacher, Student, Course

class CLI:
    def __init__(self):
        init_db()
        self.menu()

    def menu(self):
        while True:
            print("\nWelcome to the Juja Boys School Management System")
            print("1. Manage Teachers")
            print("2. Manage Students")
            print("3. Manage Courses")
            print("4. Exit")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.teacher_menu()
            elif choice == '2':
                self.student_menu()
            elif choice == '3':
                self.course_menu()
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")

    def teacher_menu(self):
        while True:
            print("\nTeachers Menu:")
            print("1. Create Teacher")
            print("2. Delete Teacher")
            print("3. View All Teachers")
            print("4. Assign Course to Teacher")
            print("5. Back to Main Menu")

            choice = input("Enter your choice: ")
            if choice == '1':
                name = input("Enter teacher name: ")
                Teacher.create(name)
                print(f"Teacher '{name}' created successfully!")
            elif choice == '2':
                teacher_id = input("Enter teacher ID to delete: ")
                Teacher.delete(teacher_id)
                print(f"Teacher with ID '{teacher_id}' deleted successfully!")
            elif choice == '3':
                teachers = Teacher.get_all()
                print("\nTeachers:")
                for teacher in teachers:
                    print(teacher)
            elif choice == '4':
                teacher_id = input("Enter teacher ID: ")
                course_id = input("Enter course ID to assign: ")
                Teacher.assign_course(teacher_id, course_id)
                print(f"Course ID '{course_id}' assigned to teacher ID '{teacher_id}' successfully!")
            elif choice == '5':
                break
            else:
                print("Invalid choice, please try again.")

    def student_menu(self):
        while True:
            print("\nStudents Menu:")
            print("1. Create Student")
            print("2. Delete Student")
            print("3. View All Students")
            print("4. View Students by Teacher ID")
            print("5. Back to Main Menu")

            choice = input("Enter your choice: ")
            if choice == '1':
                name = input("Enter student name: ")
                age = input("Enter student age: ")
                sex = input("Enter student sex: ")
                teacher_id = input("Enter teacher ID: ")
                Student.create(name, age, sex, teacher_id)
                print(f"Student '{name}' created successfully!")
            elif choice == '2':
                student_id = input("Enter student ID to delete: ")
                Student.delete(student_id)
                print(f"Student with ID '{student_id}' deleted successfully!")
            elif choice == '3':
                students = Student.get_all()
                print("\nStudents:")
                for student in students:
                    print(student)
            elif choice == '4':
                teacher_id = input("Enter teacher ID to view students: ")
                students = Student.get_by_teacher(teacher_id)
                print("\nStudents:")
                for student in students:
                    print(student)
            elif choice == '5':
                break
            else:
                print("Invalid choice, please try again.")

    def course_menu(self):
        while True:
            print("\nCourses Menu:")
            print("1. Create Course")
            print("2. Delete Course")
            print("3. View All Courses")
            print("4. View Courses by Teacher ID")
            print("5. Back to Main Menu")

            choice = input("Enter your choice: ")
            if choice == '1':
                name = input("Enter course name: ")
                teacher_id = input("Enter teacher ID: ")
                Course.create(name, teacher_id)
                print(f"Course '{name}' created successfully!")
            elif choice == '2':
                course_id = input("Enter course ID to delete: ")
                Course.delete(course_id)
                print(f"Course with ID '{course_id}' deleted successfully!")
            elif choice == '3':
                courses = Course.get_all()
                print("\nCourses:")
                for course in courses:
                    print(course)
            elif choice == '4':
                teacher_id = input("Enter teacher ID to view courses: ")
                courses = Course.get_by_teacher(teacher_id)
                print("\nCourses:")
                for course in courses:
                    print(course)
            elif choice == '5':
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    CLI()
#python cli.py