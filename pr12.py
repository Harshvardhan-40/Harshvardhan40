def Eagl():
    import tkinter as Eagl

    def go_back():
        for frame in all_pages.values():
            frame.pack_forget()
        top_frame.pack(side="top",fill="x")

    def show_contant(Q):
        # Top layout (heading + buttons) hide
        top_frame.pack_forget()

    # Hide all pages
        for J in all_pages.values():
            J.pack_forget()

    # Show selected page full window
        all_pages[Q].pack(fill="both", expand=True)

    root = Eagl.Tk()
    root.geometry("1000x1000")
    root.title("Eagl")
    root.state('zoomed')

# Top layout frame
    top_frame = Eagl.Frame(root)
    top_frame.pack(fill="both", expand=True)

# Heading inside top_frame
    L1 = Eagl.Label(top_frame, text="What Type Of Game Do You Want To Make", font=("Arial", 20))
    L1.pack(pady=20)

# Game categories
    option = [
    "Action Games", "Racing Games", "Puzzle Games",
    "Music & Rhythm Games", "Adventure Games",
    "Horror Games", "Sports Games",
    "Strategy Games", "Role-Playing Games",
]

# Buttons inside top_frame
    for H in option:
        I = Eagl.Button(top_frame, text=H, font=("Arial", 16), width=30, command=lambda c=H: show_contant(c))
        I.pack(pady=5)

# Dictionary to store content pages
    all_pages = {}


    Action_frame = Eagl.Frame(root, bg="lightblue")
    Eagl.Button(Action_frame, text="← Go Back", command=go_back,bg="lightblue").pack(anchor='nw', padx=10, pady=10)
    Eagl.Label(Action_frame, text="🎮 Action Game Making Tutorial", font=("Arial", 32), bg="lightblue").pack(expand=True)
    all_pages["Action Games"] = Action_frame


    Racing_frame = Eagl.Frame(root, bg="lightpink")
    Eagl.Button(Racing_frame, text="← Go Back", command=go_back,bg="lightpink").pack(anchor='nw', padx=10, pady=10)
    Eagl.Label(Racing_frame, text="🏎️ Racing Game Making Tutorial", font=("Arial", 32), bg="lightpink").pack(expand=True)
    all_pages["Racing Games"] = Racing_frame

    Puzzle_Games = Eagl.Frame(root, bg="lightgreen")
    Eagl.Button(Puzzle_Games, text="← Go Back", command=go_back,bg="lightgreen").pack(anchor='nw', padx=10, pady=10)
    Eagl.Label(Puzzle_Games, text="Puzzle Game Making Tutorial", font=("Arial", 32), bg="lightgreen").pack(expand=True)
    all_pages["Puzzle Games"] = Puzzle_Games

    Music_and_Phythim_game = Eagl.Frame(root, bg="red")
    Eagl.Button(Music_and_Phythim_game, text="← Go Back", command=go_back,bg="red").pack(anchor='nw', padx=10, pady=10)
    Eagl.Label(Music_and_Phythim_game, text="Music and phythim Game Making Tutorial", font=("Arial", 32), bg="red").pack(expand=True)
    all_pages["Music & Rhythm Games"] = Music_and_Phythim_game

    Advanture_game = Eagl.Frame(root, bg="yellow")
    Eagl.Button(Advanture_game, text="← Go Back", command=go_back,bg="yellow").pack(anchor='nw', padx=10, pady=10)
    Eagl.Label(Advanture_game, text="Advanture Game Making Tutorial", font=("Arial", 32), bg="yellow").pack(expand=True)
    all_pages["Adventure Games"] = Advanture_game

    Horror_game = Eagl.Frame(root, bg="orange")
    Eagl.Button(Horror_game, text="← Go Back", command=go_back,bg="orange").pack(anchor='nw', padx=10, pady=10)
    Eagl.Label(Horror_game, text="Horror Game Making Tutorial", font=("Arial", 32), bg="orange").pack(expand=True)
    all_pages["Horror Games"] = Horror_game

    sports_game = Eagl.Frame(root, bg="purple")
    Eagl.Button(sports_game, text="← Go Back", command=go_back,bg="purple").pack(anchor='nw', padx=10, pady=10)
    Eagl.Label(sports_game, text="Sports Game Making Tutorial", font=("Arial", 32), bg="purple").pack(expand=True)
    all_pages["Sports Games"] = sports_game

    Strategy_Games = Eagl.Frame(root, bg="brown")
    Eagl.Button(Strategy_Games, text="← Go Back", command=go_back,bg="brown").pack(anchor='nw', padx=10, pady=10)
    Eagl.Label(Strategy_Games, text="Strategy Game Making Tutorial", font=("Arial", 32), bg="brown").pack(expand=True)
    all_pages["Strategy Games"] = Strategy_Games

    Role_playing_game = Eagl.Frame(root, bg="green")
    Eagl.Button(Role_playing_game, text="← Go Back", command=go_back,bg="green").pack(anchor='nw', padx=10, pady=10)
    Eagl.Label(Role_playing_game, text="Role-Playing Games Making Tutorial", font=("Arial", 32), bg="green").pack(expand=True)
    all_pages["Role-Playing Games"] = Role_playing_game


import tkinter as tk
from tkinter import messagebox

# Function to open new window (next page)


# Submit function with validation
def submit():
    first = first_name_entry.get().strip()
    last = last_name_entry.get().strip()

    if not first or not last:
        messagebox.showerror("Input Error", "Please enter both First Name and Last Name.")
    else:
        Eagl()

# Main Window
root = tk.Tk()
root.title("Name Validator")
root.geometry("300x200")

tk.Label(root, text="First Name").pack(pady=5)
first_name_entry = tk.Entry(root)
first_name_entry.pack()

tk.Label(root, text="Last Name").pack(pady=5)
last_name_entry = tk.Entry(root)
last_name_entry.pack()

tk.Button(root, text="Submit", command=submit).pack(pady=20)

root.mainloop()
