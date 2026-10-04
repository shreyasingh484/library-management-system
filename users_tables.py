import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

# Insert a sample user
cursor.execute("""
INSERT INTO users (username, password)
VALUES (?, ?)
""", ("admin", "admin123"))

conn.commit()
conn.close()

print("Users table created successfully!")