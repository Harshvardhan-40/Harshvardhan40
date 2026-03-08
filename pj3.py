import tkinter as Eagl

def go_back():
    for frame in all_pages.values():
        frame.pack_forget()
    top_frame.pack(side="top",fill='x')



def show_contact(Q):
    top_frame.pack_forget()

    for h in all_pages.values():
        h.pack_forget()

    all_pages[Q].pack(fill="both", expand=True)


root = Eagl.Tk()
root.geometry("1000x1000")
root.title("Eagl")

top_frame = Eagl.Frame(root)
top_frame.pack(fill='both',expand=True)

l1 = Eagl.Label(top_frame, text="What Type Of Education Do You Want", font=('Arial',30))
l1.pack(pady=30)

option = ["Formal Education","Informal Education","Digital/Online Education",
          "Non-Formal Education","Technical and Vocational Education"]

for ed in option:
    e = Eagl.Button(top_frame, text=ed, font=('Arial', 14), width=30, command=lambda c=ed: show_contact(c))
    e.pack(pady=5)

all_pages = {}

formal_frame = Eagl.Frame(root,bg="lightblue")
Eagl.Button(formal_frame,text="← Go Back",command=go_back,bg="lightblue").pack(anchor='nw',padx=5,pady=5)
Eagl.Label(formal_frame, text="Formal Education learning", font=("Arial", 32), bg="lightblue").pack(expand=True)
all_pages["Formal Education"] = formal_frame

Informal_education = Eagl.Frame(root,bg="blue")
Eagl.Button(Informal_education,text="← Go Back",command=go_back,bg='blue').pack(anchor='nw',padx=10,pady=10)
Eagl.Label(Informal_education,text="Informal Eduacation Learning",font=('Arial', 30),bg='blue').pack(expand=True)
all_pages["Informal Education"] = Informal_education

e = Eagl.Frame(root,bg="green")
Eagl.Button(e,text="← Go Back",command=go_back,bg='green').pack(anchor='nw',padx=10,pady=10)
Eagl.Label(e,text="Non-Formal Eduacation Learning",font=('Arial', 30),bg='green').pack(expand=True)
all_pages["Non-Formal Education"] = e

D = Eagl.Frame(root,bg="pink")
Eagl.Button(D,text="← Go Back",command=go_back,bg='pink').pack(anchor='nw',padx=10,pady=10)
Eagl.Label(D,text="Digital/Online Education Learning",font=('Arial', 30),bg='pink').pack(expand=True)
all_pages["Digital/Online Education"] = D

z = Eagl.Frame(root,bg="orange")
Eagl.Button(z,text="← Go Back",command=go_back,bg='orange').pack(anchor='nw',padx=10,pady=10)
Eagl.Label(z,text="Technical and Vocational Education Learning",font=('Arial', 30),bg='orange').pack(expand=True)
all_pages["Technical and Vocational Education"] = z

root.mainloop()
