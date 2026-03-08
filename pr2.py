import tkinter as tk
from tkinter import ttk

def on_select(event):
    selected_option = combo.get()
    if selected_option == "होम":
        label.config(text="यह होम पेज है")
    elif selected_option == "सेटिंग":
        label.config(text="यह सेटिंग पेज है")
    elif selected_option == "अबाउट":
        label.config(text="यह अबाउट पेज है")

root = tk.Tk()
root.title("Combobox Example")
root.geometry("400x200")

# Dropdown / Combobox
options = ["होम", "सेटिंग", "अबाउट"]
combo = ttk.Combobox(root, values=options, state="readonly")
combo.set("कोई विकल्प चुनें")
combo.pack(pady=20)

# Label to show page content
label = tk.Label(root, text="", font=("Arial", 14))
label.pack(pady=20)

# Bind combobox selection
combo.bind("<<ComboboxSelected>>", on_select)

root.mainloop()
