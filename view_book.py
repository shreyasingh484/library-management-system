import sqlite3

def view_books():
    # Connect to database
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    # Fetch all books from database
    cursor.execute("SELECT id, title, author, category, quantity FROM books")
    books = cursor.fetchall()

    if len(books) == 0:
        print("No books found in the library.")
    else:
        print("Books in the library:")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Category: {book[3]}, Quantity: {book[4]}")

    connection.close()