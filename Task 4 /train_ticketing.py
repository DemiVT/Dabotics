import sqlite3

def create_table():
    conn = sqlite3.connect('ticketing.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        passenger_name TEXT,
        train_number TEXT,
        seat_number TEXT,
        status TEXT
    )
    ''')
    conn.commit()
    conn.close()

def book_ticket(passenger_name, train_number, seat_number):
    conn = sqlite3.connect('ticketing.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO tickets (passenger_name, train_number, seat_number, status)
    VALUES (?, ?, ?, ?)
    ''', (passenger_name, train_number, seat_number, 'Booked'))
    conn.commit()
    conn.close()

def cancel_ticket(id):
    conn = sqlite3.connect('ticketing.db')
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE tickets
    SET status = 'Cancelled'
    WHERE id = ?
    ''', (id,))
    conn.commit()
    conn.close()

def view_bookings():
    conn = sqlite3.connect('ticketing.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM tickets
    ''')
    records = cursor.fetchall()
    conn.close()
    return records

# Create table
create_table()

# Example usage
book_ticket('Alice', '1234', 'A1')
print(view_bookings())
cancel_ticket(1)
print(view_bookings())
