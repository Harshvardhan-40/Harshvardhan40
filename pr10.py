import smtplib
import tkinter as tk
from tkinter import messagebox

def verify_login():
    email = email_entry.get()
    password = password_entry.get()

    if not email or not password:
        messagebox.showerror("Error", "Please enter both email and password.")
        return

    try:
        print("Trying to connect to Gmail SMTP server...")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        print("Trying to login...")
        server.login(email, password)
        server.quit()
        print("Login successful!")
        messagebox.showinfo("Login Success", "Gmail login successful!")
        open_next_page()
    except smtplib.SMTPAuthenticationError as auth_err:
        print(f"SMTPAuthenticationError: {auth_err}")
        messagebox.showerror("Login Failed", "Invalid Gmail or App Password.\nMake sure you are using App Password.")
    except Exception as e:
        print(f"General Exception: {e}")
        messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")

def open_next_page():
    next_window = tk.Toplevel(root)
    next_window.title("Next Step")
    tk.Label(next_window, text="Welcome! You are logged in.").pack(pady=20)
    tk.Button(next_window, text="Close", command=next_window.destroy).pack()

# ------------------ GUI ------------------ #
root = tk.Tk()
root.title("Gmail Login Check")

tk.Label(root, text="Enter Gmail:").pack()
email_entry = tk.Entry(root, width=40)
email_entry.pack()

tk.Label(root, text="Enter App Password:").pack()
password_entry = tk.Entry(root, show="*", width=40)
password_entry.pack()

tk.Button(root, text="Login & Proceed", command=verify_login).pack(pady=10)

root.mainloop()
