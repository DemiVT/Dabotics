import sqlite3

def create_table():
    conn = sqlite3.connect('bug_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bugs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        assigned_to TEXT,
        priority TEXT,
        status TEXT
    )
    ''')
    conn.commit()
    conn.close()

def log_bug(description, assigned_to, priority):
    conn = sqlite3.connect('bug_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO bugs (description, assigned_to, priority, status)
    VALUES (?, ?, ?, ?)
    ''', (description, assigned_to, priority, 'Open'))
    conn.commit()
    conn.close()

def update_bug(id, status):
    conn = sqlite3.connect('bug_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE bugs
    SET status = ?
    WHERE id = ?
    ''', (status, id))
    conn.commit()
    conn.close()

# Create table
create_table()

# Example usage
log_bug('Error in login module', 'Alice', 'High')
update_bug(1, 'Resolved')
