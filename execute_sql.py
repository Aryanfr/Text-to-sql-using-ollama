import sqlite3

def execute_sql_query(query):
    try:
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        # Execute the query
        cursor.execute(query)
        rows = cursor.fetchall()

        conn.close()
        return rows
    except sqlite3.Error as e:
        print(f"SQL Execution Error: {e}")
        return None