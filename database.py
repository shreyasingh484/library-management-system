import sqlite3

# Connect to database
connection = sqlite3.connect("library.db")
cursor = connection.cursor()

# Create books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    category TEXT,
    quantity INTEGER NOT NULL
)
""")

# Create issued_books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS issued_books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_title TEXT NOT NULL,
    student_name TEXT NOT NULL
)
""")

# Save changes
connection.commit()

# Close connection
connection.close()

print("Database and tables created successfully.")