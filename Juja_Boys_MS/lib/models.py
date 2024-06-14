import sqlite3
from helpers import execute_query, fetch_all, fetch_one

def init_db():
    create_teacher_table = '''
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    '''
    
    create_student_table = '''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        sex TEXT,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teachers (id)
    );
    '''

    create_course_table = '''
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teachers (id)
    );
    '''
    
    execute_query(create_teacher_table)
    execute_query(create_student_table)
    execute_query(create_course_table)

class Teacher:
    @staticmethod
    def create(name):
        query = 'INSERT INTO teachers (name) VALUES (?);'
        execute_query(query, (name,))
    
    @staticmethod
    def delete(teacher_id):
        query = 'DELETE FROM teachers WHERE id = ?;'
        execute_query(query, (teacher_id,))
    
    @staticmethod
    def get_all():
        query = 'SELECT * FROM teachers;'
        return fetch_all(query)
    
    @staticmethod
    def assign_course(teacher_id, course_id):
        query = 'UPDATE courses SET teacher_id = ? WHERE id = ?;'
        execute_query(query, (teacher_id, course_id))

class Student:
    @staticmethod
    def create(name, age, sex, teacher_id):
        query = '''
        INSERT INTO students (name, age, sex, teacher_id) 
        VALUES (?, ?, ?, ?);
        '''
        execute_query(query, (name, age, sex, teacher_id))

    @staticmethod
    def delete(student_id):
        query = 'DELETE FROM students WHERE id = ?;'
        execute_query(query, (student_id,))

    @staticmethod
    def get_all():
        query = 'SELECT * FROM students;'
        return fetch_all(query)

    @staticmethod
    def get_by_teacher(teacher_id):
        query = 'SELECT * FROM students WHERE teacher_id = ?;'
        return fetch_all(query, (teacher_id,))

class Course:
    @staticmethod
    def create(name, teacher_id):
        query = 'INSERT INTO courses (name, teacher_id) VALUES (?, ?);'
        execute_query(query, (name, teacher_id))
    
    @staticmethod
    def delete(course_id):
        query = 'DELETE FROM courses WHERE id = ?;'
        execute_query(query, (course_id,))
    
    @staticmethod
    def get_all():
        query = 'SELECT * FROM courses;'
        return fetch_all(query)
    
    @staticmethod
    def get_by_teacher(teacher_id):
        query = 'SELECT * FROM courses WHERE teacher_id = ?;'
        return fetch_all(query, (teacher_id,))
