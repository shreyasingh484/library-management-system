import sqlite3

def add_book(title, author, category, quantity):
    # Connect to database
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    # Insert book into database
    cursor.execute("""
    INSERT INTO books (title, author, category, quantity)
    VALUES (?, ?, ?, ?)
    """, (title, author, category, quantity))

    # Save changes and close connection
    connection.commit()
    connection.close()

    print(f"Book '{title}' by {author} added successfully.")