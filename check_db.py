import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

print(users)

conn.close()