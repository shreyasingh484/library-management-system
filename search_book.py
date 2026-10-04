import sqlite3

def search_book(title):
    # Connect to database
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    # Search for book by title
    cursor.execute(
        "SELECT * FROM books WHERE title LIKE ?", ('%' + title + '%',))
    
    books = cursor.fetchall()

    if len(books) == 0:
        print(f"No books found with title containing '{title}'.")
    else:
        print(f"Books found with title containing '{title}':")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Category: {book[3]}, Quantity: {book[4]}")

    connection.close()