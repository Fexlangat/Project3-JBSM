import sqlite3

def execute_query(query, params=()):
    try:
        with sqlite3.connect('school.db') as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def fetch_all(query, params=()):
    try:
        with sqlite3.connect('school.db') as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []

def fetch_one(query, params=()):
    try:
        with sqlite3.connect('school.db') as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None
