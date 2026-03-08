import tkinter as tk
from tkinter import messagebox

# Function to open new window based on selection

# Name and Last Name Labels and Entry Fields








def open_page():


    choice = var.get()
    if choice == 1:
        page1()
    elif choice == 2:
        page2()
    elif choice == 3:
        page3()
    else:
        messagebox.showwarning("Warning", "Please select an option!")

# Page 1
def page1():
    new_win = tk.Toplevel(root)
    new_win.title("Page 1")
    tk.Label(new_win, text="This is Page 1", font=("Arial", 16)).pack(pady=20)

# Page 2
def page2():
    new_win = tk.Toplevel(root)
    new_win.title("Page 2")
    tk.Label(new_win, text="This is Page 2", font=("Arial", 16)).pack(pady=20)

# Page 3
def page3():
    new_win = tk.Toplevel(root)
    new_win.title("Page 3")
    tk.Label(new_win, text="This is Page 3", font=("Arial", 16)).pack(pady=20)

# Main Window
root = tk.Tk()
root.title("Radio Button Navigation")
root.geometry("300x250")

tk.Label(root, text="Select a Page:", font=("Arial", 14)).pack(pady=10)
tk.Label(root, text="First Name:", font=("Arial", 12)).pack(pady=2)
first_name_entry = tk.Entry(root, font=("Arial", 12))
first_name_entry.pack(pady=2)

tk.Label(root, text="Last Name:", font=("Arial", 12)).pack(pady=2)
last_name_entry = tk.Entry(root, font=("Arial", 12))
last_name_entry.pack(pady=2)

# Radio buttons
var = tk.IntVar()
tk.Radiobutton(root, text="Open Page 1", variable=var, value=1, font=("Arial", 12)).pack(anchor="w")
tk.Radiobutton(root, text="Open Page 2", variable=var, value=2, font=("Arial", 12)).pack(anchor="w")
tk.Radiobutton(root, text="Open Page 3", variable=var, value=3, font=("Arial", 12)).pack(anchor="w")

# Submit Button
tk.Button(root, text="Submit", command=open_page, font=("Arial", 12), bg="blue", fg="white").pack(pady=20)

root.mainloop()
