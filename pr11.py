import tkinter as tk
from tkinter import messagebox

def submit():
    first = first_name_entry.get().strip()
    last = last_name_entry.get().strip()

    if not first or not last:
        messagebox.showerror("Input Error", "Please enter both First Name and Last Name.")
    else:
        messagebox.showinfo("Success", f"Hello, {first} {last}!")

# Main window
root = tk.Tk()
root.title("Name Validator")
root.geometry("300x200")

# First Name
tk.Label(root, text="First Name").pack(pady=5)
first_name_entry = tk.Entry(root)
first_name_entry.pack()

# Last Name
tk.Label(root, text="Last Name").pack(pady=5)
last_name_entry = tk.Entry(root)
last_name_entry.pack()

# Submit Button
tk.Button(root, text="Submit", command=submit).pack(pady=20)

# Run the application
root.mainloop()
