import sqlite3

def initialize_database():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    # Create students table if not exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        grade INTEGER
    );
    """)

    # Insert sample data
    cursor.executemany("""
    INSERT INTO students (name, grade) VALUES (?, ?);
    """, [
        ("Alice", 95),
        ("Bob", 85),
        ("Charlie", 90),
        ("Diana", 92)
    ])

    connection.commit()
    connection.close()

initialize_database()
print("Database initialized successfully.")