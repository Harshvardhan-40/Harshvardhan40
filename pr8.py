import tkinter as tk

def open_tutorial(user_name):
    tutorial_win = tk.Toplevel()
    tutorial_win.geometry("1000x1000")
    tutorial_win.title("Eagl")

    def go_back():
        for frame in all_pages.values():
            frame.pack_forget()
        top_frame.pack(fill="both", expand=True)

    def show_content(category):
        top_frame.pack_forget()
        for frame in all_pages.values():
            frame.pack_forget()
        all_pages[category].pack(fill="both", expand=True)

    top_frame = tk.Frame(tutorial_win)
    top_frame.pack(fill="both", expand=True)

    # Display the user's name at the top
    name_label = tk.Label(top_frame, text=f"Welcome, {user_name}!", font=("Arial", 24), fg="blue")
    name_label.pack(pady=10)

    heading = tk.Label(top_frame, text="What Type Of Game Do You Want To Make", font=("Arial", 20))
    heading.pack(pady=20)

    options = [
        "Action Games", "Racing Games", "Puzzle Games",
        "Music & Rhythm Games", "Adventure Games",
        "Horror Games", "Sports Games",
        "Strategy Games", "Role-Playing Games",
    ]

    for option in options:
        btn = tk.Button(top_frame, text=option, font=("Arial", 16), width=30,
                        command=lambda c=option: show_content(c))
        btn.pack(pady=5)

    all_pages = {}

    def create_page(name, bg_color, label_text):
        frame = tk.Frame(tutorial_win, bg=bg_color)
        tk.Button(frame, text="← Go Back", command=go_back, bg=bg_color).pack(anchor='nw', padx=10, pady=10)
        tk.Label(frame, text=label_text, font=("Arial", 32), bg=bg_color).pack(expand=True)
        all_pages[name] = frame

    create_page("Action Games", "lightblue", "🎮 Action Game Making Tutorial")
    create_page("Racing Games", "lightpink", "🏎️ Racing Game Making Tutorial")
    create_page("Puzzle Games", "lightgreen", "Puzzle Game Making Tutorial")
    create_page("Music & Rhythm Games", "red", "Music and Rhythm Game Making Tutorial")
    create_page("Adventure Games", "yellow", "Adventure Game Making Tutorial")
    create_page("Horror Games", "orange", "Horror Game Making Tutorial")
    create_page("Sports Games", "purple", "Sports Game Making Tutorial")
    create_page("Strategy Games", "brown", "Strategy Game Making Tutorial")
    create_page("Role-Playing Games", "green", "Role-Playing Games Making Tutorial")

    tutorial_win.mainloop()

# Main window
root = tk.Tk()
root.geometry("300x400")
root.title("Eagl")

tk.Label(root, text="EAGL", font=("Arial", 30)).pack(pady=25)

tk.Label(root, text="Enter Your Name").pack()
name_entry = tk.Entry(root, font=("Arial", 16), bd=1)
name_entry.pack(pady=10)

tk.Label(root, text="Enter Your Last Name").pack()
last_name_entry = tk.Entry(root, font=("Arial", 16), bd=1)
last_name_entry.pack(pady=10)

tk.Label(root, text="Why Did You Choose Eagl?").pack(pady=10)

selected_option = tk.IntVar(value=0)
options = ["Education", "Gaming", "Social Media"]

for idx, option_text in enumerate(options, 1):
    tk.Radiobutton(root, text=option_text, variable=selected_option, value=idx).pack()

def submit():
    user_name = name_entry.get().strip()
    if user_name == "":
        user_name = "Guest"
    open_tutorial(user_name)

submit_btn = tk.Button(root, text="SUBMIT", font=("Arial", 16), command=submit)
submit_btn.pack(pady=40)

root.mainloop()
