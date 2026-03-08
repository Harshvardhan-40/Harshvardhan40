import tkinter as Eagl

root = Eagl.Tk()
root.geometry("300x400")
root.title("Eagl")



l3 = Eagl.Label(text="EAGL",font=100)
l3.pack(pady=25)

label = Eagl.Label(text="Enter your First Name")
label.pack()

name = Eagl.Entry(root, font=('Arial',10), bd=1)
name.pack(pady=10)

p1 = Eagl.Label(text=" Enter your last Name ")
p1.pack()

pe1 = Eagl.Entry(root)
pe1.pack(pady=10)

l2 = Eagl.Label(text="Why Are You Choose Eagl")
l2.pack(pady=10)

selected_option = Eagl.IntVar(value=0)

options = ["Education", "Gamming", "Social Media"]

for idx, text in enumerate(options, 1):
    Eagl.Radiobutton(root, text=text, variable=selected_option, value=idx).pack()


b1 = Eagl.Button(text="SUBMIT",font=35)
b1.pack(pady=40)

root.mainloop()


