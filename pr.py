import tkinter as Eagl

def show_contant(Q):
    top_frame.pack_forget()


    for J in all_pages.values():
        J.pack_forget()

    all_pages[Q].pack(fill = "both",expand = True)


root = Eagl.Tk()
root.geometry("1000x1000")
root.title("Eagl")

top_frame = Eagl.Frame(root)
top_frame.pack(fill="both",expand=True )




L1 = Eagl.Label(text="What Type Of Game Do You Want To Make",font=('Arial',20))
L1.pack(pady=20)
option = [
    "Action Games", "Racing Games", "Puzzle Games",
    "Music & Rhythm Games", "Adventure Games",
    "Horror Games", "Sports Games",
    "Strategy Games", "Role-Playing Games",
]

for H in option:
    I = Eagl.Button(root ,text=H,font=('Arial',16),width=30,command=lambda c=H: show_contant(c))
    I.pack()

all_pages = {}

Action_frame = Eagl.Frame(root,bg="lightblue")
Eagl.Label(Action_frame,text="Action Game Make Learning",font=("Arial",32),background="lightblue").pack(expand=True)
all_pages["Action Games"] = Action_frame
back_button = Eagl.Button(root, text="← Back", command=root.destroy)
back_button.pack(anchor='nw', padx=10, pady=10)




Racing_frame = Eagl.Frame(root,bg="lightpink")
Eagl.Label(Racing_frame,text="Racing Game Make Leaning",font=("Arial",32),background="lightpink").pack(expand=True)
all_pages["Racing Games"] = Racing_frame



root.mainloop()