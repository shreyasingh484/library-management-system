import sqlite3

def issue_book(book_title, student_name):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO issued_books (book_title, student_name) VALUES (?, ?)",
        (book_title, student_name)
    )

    connection.commit()
    connection.close()

    print("Book issued successfully!")

def return_book(book_title, student_name):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM issued_books WHERE book_title=? AND student_name=?",
        (book_title, student_name)
    )

    connection.commit()
    connection.close()

    print("Book returned successfully!")