import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

window.title("Library Management System")
window.geometry("500x450")
from tkinter import messagebox

from add_book import add_book
from view_book import view_books
from search_book import search_book
from issue_book import issue_book, return_book
from delete_book import delete_book


# ---------------- Add Book ----------------

def open_add_book():
    add_window = tk.Toplevel(window)
    add_window.title("Add Book")
    add_window.geometry("300x300")

    tk.Label(add_window, text="Title").pack()
    title_entry = tk.Entry(add_window)
    title_entry.pack()

    tk.Label(add_window, text="Author").pack()
    author_entry = tk.Entry(add_window)
    author_entry.pack()

    tk.Label(add_window, text="Category").pack()
    category_entry = tk.Entry(add_window)
    category_entry.pack()

    tk.Label(add_window, text="Quantity").pack()
    quantity_entry = tk.Entry(add_window)
    quantity_entry.pack()

    def save_book():
        try:
            add_book(
                title_entry.get(),
                author_entry.get(),
                category_entry.get(),
                int(quantity_entry.get())
            )
            messagebox.showinfo("Success", "Book added successfully!")
            add_window.destroy()

        except ValueError:
            messagebox.showerror("Error", "Quantity must be a number")

    tk.Button(add_window, text="Save", command=save_book).pack(pady=10)


# ---------------- Search Book ----------------

def open_search_book():
    search_window = tk.Toplevel(window)
    search_window.title("Search Book")
    search_window.geometry("300x200")

    tk.Label(search_window, text="Enter Book Title").pack()

    search_entry = tk.Entry(search_window)
    search_entry.pack()

    def perform_search():
        search_book(search_entry.get())

    tk.Button(
        search_window,
        text="Search",
        command=perform_search
    ).pack(pady=10)


# ---------------- Issue Book ----------------

def open_issue_book():
    issue_window = tk.Toplevel(window)
    issue_window.title("Issue Book")
    issue_window.geometry("300x200")

    tk.Label(issue_window, text="Book Title").pack()
    book_entry = tk.Entry(issue_window)
    book_entry.pack()

    tk.Label(issue_window, text="Student Name").pack()
    student_entry = tk.Entry(issue_window)
    student_entry.pack()

    def issue():
        issue_book(
            book_entry.get(),
            student_entry.get()
        )
        messagebox.showinfo("Success", "Book issued successfully!")
        issue_window.destroy()

    tk.Button(issue_window, text="Issue", command=issue).pack(pady=10)


# ---------------- Return Book ----------------

def open_return_book():
    return_window = tk.Toplevel(window)
    return_window.title("Return Book")
    return_window.geometry("300x200")

    tk.Label(return_window, text="Book Title").pack()
    book_entry = tk.Entry(return_window)
    book_entry.pack()

    tk.Label(return_window, text="Student Name").pack()
    student_entry = tk.Entry(return_window)
    student_entry.pack()

    def return_b():
        return_book(
            book_entry.get(),
            student_entry.get()
        )
        messagebox.showinfo("Success", "Book returned successfully!")
        return_window.destroy()

    tk.Button(
        return_window,
        text="Return",
        command=return_b
    ).pack(pady=10)


# ---------------- Delete Book ----------------

def open_delete_book():
    delete_window = tk.Toplevel(window)
    delete_window.title("Delete Book")
    delete_window.geometry("300x150")

    tk.Label(delete_window, text="Book Title").pack()

    title_entry = tk.Entry(delete_window)
    title_entry.pack()

    def delete():
        delete_book(title_entry.get())
        messagebox.showinfo("Success", "Book deleted successfully!")
        delete_window.destroy()

    tk.Button(
        delete_window,
        text="Delete",
        command=delete
    ).pack(pady=10)


# ---------------- Main Window ----------------


heading = tk.Label(
    window,
    text="Library Management System",
    font=("Arial", 16)
)
heading.pack(pady=20)

# Add Book
tk.Button(
    window,
    text="Add Book",
    width=25,
    command=open_add_book
).pack(pady=5)

# View Books
tk.Button(
    window,
    text="View Books",
    width=25,
    command=view_books
).pack(pady=5)

# Search Book
tk.Button(
    window,
    text="Search Book",
    width=25,
    command=open_search_book
).pack(pady=5)

# Issue Book
tk.Button(
    window,
    text="Issue Book",
    width=25,
    command=open_issue_book
).pack(pady=5)

# Return Book
tk.Button(
    window,
    text="Return Book",
    width=25,
    command=open_return_book
).pack(pady=5)

# Delete Book
tk.Button(
    window,
    text="Delete Book",
    width=25,
    command=open_delete_book
).pack(pady=5)

# Exit
tk.Button(
    window,
    text="Exit",
    width=25,
    command=window.destroy
).pack(pady=5)

window.mainloop()