

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


    root.mainloop()

def Eagl2():
    import tkinter as Eagl2

    def go_back():
        for frame in all_pages.values():
            frame.pack_forget()
        top_frame.pack(side="top",fill='x')



    def show_contact(Q):
        top_frame.pack_forget()

        for h in all_pages.values():
            h.pack_forget()

        all_pages[Q].pack(fill="both", expand=True)


    root = Eagl2.Tk()
    root.title("Eagl")

    top_frame = Eagl2.Frame(root)
    top_frame.pack(fill='both',expand=True)

    l1 = Eagl2.Label(top_frame, text="What Type Of Education Do You Want", font=('Arial',30))
    l1.pack(pady=30)

    option = ["Formal Education","Informal Education","Digital/Online Education",
          "Non-Formal Education","Technical and Vocational Education"]

    for ed in option:
        e = Eagl2.Button(top_frame, text=ed, font=('Arial', 14), width=30, command=lambda c=ed: show_contact(c))
        e.pack(pady=5)

    all_pages = {}

    formal_frame = Eagl2.Frame(root,bg="lightblue")
    Eagl2.Button(formal_frame,text="← Go Back",command=go_back,bg="lightblue").pack(anchor='nw',padx=5,pady=5)
    Eagl2.Label(formal_frame, text="Formal Education learning", font=("Arial", 32), bg="lightblue").pack(expand=True)
    all_pages["Formal Education"] = formal_frame

    Informal_education = Eagl2.Frame(root,bg="blue")
    Eagl2.Button(Informal_education,text="← Go Back",command=go_back,bg='blue').pack(anchor='nw',padx=10,pady=10)
    Eagl2.Label(Informal_education,text="Informal Eduacation Learning",font=('Arial', 30),bg='blue').pack(expand=True)
    all_pages["Informal Education"] = Informal_education

    e = Eagl2.Frame(root,bg="green")
    Eagl2.Button(e,text="← Go Back",command=go_back,bg='green').pack(anchor='nw',padx=10,pady=10)
    Eagl2.Label(e,text="Non-Formal Eduacation Learning",font=('Arial', 30),bg='green').pack(expand=True)
    all_pages["Non-Formal Education"] = e

    D = Eagl2.Frame(root,bg="pink")
    Eagl2.Button(D,text="← Go Back",command=go_back,bg='pink').pack(anchor='nw',padx=10,pady=10)
    Eagl2.Label(D,text="Digital/Online Education Learning",font=('Arial', 30),bg='pink').pack(expand=True)
    all_pages["Digital/Online Education"] = D

    z = Eagl2.Frame(root,bg="orange")
    Eagl2.Button(z,text="← Go Back",command=go_back,bg='orange').pack(anchor='nw',padx=10,pady=10)
    Eagl2.Label(z,text="Technical and Vocational Education Learning",font=('Arial', 30),bg='orange').pack(expand=True)
    all_pages["Technical and Vocational Education"] = z

    root.mainloop()





import tkinter as Eagl1
from tkinter import messagebox

def submit():
    first = name.get().strip()
    last = pe1.get().strip()

    if not first or not last:
        messagebox.showerror("Input Error", "Please enter both First Name and Last Name.")
        return False
    return True

def open():
    choice = var.get()
    if choice == 1:
        Eagl()
    elif choice == 2:
        Eagl2()
    else:
        messagebox.showwarning("Selection Missing", "Please select an option (Gamming or Education)")

def do():
    if submit():
        root.destroy()
        open()

root = Eagl1.Tk()
root.geometry("300x400")
root.title("Eagl")

Eagl1.Label(text="EAGL", font=("Arial", 20)).pack(pady=25)

Eagl1.Label(text="Enter Your Name").pack()
name = Eagl1.Entry(root, font=("Arial", 12), bd=1)
name.pack(pady=10)

Eagl1.Label(text="Enter Your Last Name").pack()
pe1 = Eagl1.Entry(root, font=("Arial", 12))
pe1.pack(pady=10)

Eagl1.Label(text="Why Are You Choosing EAGL").pack(pady=10)

var = Eagl1.IntVar(value=0)  # Correct IntVar

Eagl1.Radiobutton(root, text="Gamming", variable=var, value=1, font=('Arial', 14)).pack(anchor='w')
Eagl1.Radiobutton(root, text="Education", variable=var, value=2, font=('Arial', 14)).pack(anchor='w')

Eagl1.Button(text="SUBMIT", font=("Arial", 14), command=do).pack(pady=40)

root.mainloop()
