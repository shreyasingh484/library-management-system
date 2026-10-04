import sqlite3

def delete_book(book_id):
    # Connect to database
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    # Delete book from database
    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))

    # Save changes and close connection
    connection.commit()
    connection.close()