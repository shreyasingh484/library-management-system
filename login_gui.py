import tkinter as tk
from tkinter import messagebox
from login import login

def check_login():
    username = username_entry.get()
    password = password_entry.get()

    if login(username, password):
        messagebox.showinfo("Success", "Login Successful")
        root.destroy()
        import gui
    else:
        messagebox.showerror(
            "Error",
            "Invalid Username or Password"
        )

root = tk.Tk()
root.title("Library Login")
root.geometry("300x200")

tk.Label(root, text="Username").pack(pady=5)

username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password").pack(pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(
    root,
    text="Login",
    command=check_login
).pack(pady=20)

root.mainloop()