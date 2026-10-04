import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute(
    "INSERT INTO users(username, password) VALUES(?, ?)",
    ("shreyakhagta", "shreya")
)

conn.commit()
conn.close()

print("User added successfully")