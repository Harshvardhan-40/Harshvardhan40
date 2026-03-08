import tkinter as tk
from tkinter import ttk

def show_page(event):
    selected = combo.get()
    
    # पहले सभी पेजों को छिपाएँ
    for frame in pages.values():
        frame.pack_forget()
    
    # चुने हुए पेज को दिखाएँ
    pages[selected].pack(fill='both', expand=True)

root = tk.Tk()
root.title("Dropdown Based Pages")
root.geometry("400x300")

# Dropdown menu
options = ["होम", "सेटिंग", "अबाउट"]
combo = ttk.Combobox(root, values=options, state="readonly")
combo.set("पेज चुनें")
combo.pack(pady=10)

# पेज फ्रेम बनाएँ
pages = {}

# होम पेज
home_frame = tk.Frame(root, bg="lightblue")
tk.Label(home_frame, text="यह होम पेज है", font=("Arial", 16), bg="lightblue").pack(pady=30)
pages["होम"] = home_frame

# सेटिंग पेज
setting_frame = tk.Frame(root, bg="lightgreen")
tk.Label(setting_frame, text="यह सेटिंग पेज है", font=("Arial", 16), bg="lightgreen").pack(pady=30)
pages["सेटिंग"] = setting_frame

# अबाउट पेज
about_frame = tk.Frame(root, bg="lightyellow")
tk.Label(about_frame, text="यह अबाउट पेज है", font=("Arial", 16), bg="lightyellow").pack(pady=30)
pages["अबाउट"] = about_frame

# जब combobox से चुना जाए
combo.bind("<<ComboboxSelected>>", show_page)

root.mainloop()
