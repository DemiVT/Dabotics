import sqlite3

def create_table():
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        date TEXT,
        status TEXT
    )
    ''')
    conn.commit()
    conn.close()

def mark_attendance(name, date, status):
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO attendance (name, date, status)
    VALUES (?, ?, ?)
    ''', (name, date, status))
    conn.commit()
    conn.close()

def get_attendance(name):
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT date, status FROM attendance WHERE name = ?
    ''', (name,))
    records = cursor.fetchall()
    conn.close()
    return records

# Create table
create_table()

# Example usage
mark_attendance('John Doe', '2024-09-08', 'Present')
print(get_attendance('John Doe'))
