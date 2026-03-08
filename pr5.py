import tkinter as tk

def option_selected(choice):
    if choice == "होम":
        label.config(text="यह होम पेज है")
    elif choice == "सेटिंग":
        label.config(text="यह सेटिंग पेज है")
    elif choice == "प्रोफाइल":
        label.config(text="यह प्रोफाइल पेज है")
    else:
        label.config(text="कोई विकल्प चुना नहीं गया")

root = tk.Tk()
root.geometry("400x250")
root.title("OptionMenu Example")

options = ["होम", "सेटिंग", "प्रोफाइल"]
selected_option = tk.StringVar()
selected_option.set("विकल्प चुनें")  # default text

dropdown = tk.OptionMenu(root, selected_option, *options, command=option_selected)
dropdown.pack(pady=20)

label = tk.Label(root, text="", font=("Arial", 14))
label.pack(pady=30)

root.mainloop()
