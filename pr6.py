import tkinter as tk

def go_back():
    for frame in all_pages.values():
        frame.pack_forget()
    top_frame.pack(side="right",fill="x")


def show_content(category):
    # ऊपर के सभी बटन वाला frame छिपा दो
    top_frame.pack_forget()
    
    # सभी pages को छिपाओ
    for frame in all_pages.values():
        frame.pack_forget()
    
    # चुना गया content पूरे window में दिखाओ
    all_pages[category].pack(fill='both', expand=True)

root = tk.Tk()
root.geometry("500x400")
root.title("Category Selector Example")

# --- Top Frame for buttons ---
top_frame = tk.Frame(root)
top_frame.pack(side="top", fill="x")

# --- Content Frame (visible only after selection) ---
all_pages = {}

# --- Buttons ---
categories = ["Action", "Gaming", "Education"]

for cat in categories:
    btn = tk.Button(top_frame, text=cat, width=12, command=lambda c=cat: show_content(c))
    btn.pack(side="left", padx=5, pady=5)

# --- Action Page ---

action_frame = tk.Frame(root, bg="lightblue")

# पहले Go Back बटन पैक करें (top-left)
tk.Button(action_frame, text="← Go Back", command=go_back).pack(anchor='nw', padx=10, pady=10)

# फिर label जो बाकी जगह लेता है
tk.Label(action_frame, text="🎬 Action से संबंधित कंटेंट", font=("Arial", 18), bg="lightblue").pack(expand=True)

# dictionary में जोड़ो
all_pages["Action"] = action_frame



# --- Gaming Page ---
gaming_frame = tk.Frame(root, bg="lightgreen")
tk.Label(gaming_frame, text="🎮 Gaming से संबंधित कंटेंट", font=("Arial", 18), bg="lightgreen").pack(expand=True)
all_pages["Gaming"] = gaming_frame

# --- Education Page ---
edu_frame = tk.Frame(root, bg="lightyellow")
tk.Label(edu_frame, text="📚 Education से संबंधित कंटेंट", font=("Arial", 18), bg="lightyellow").pack(expand=True)
all_pages["Education"] = edu_frame

# ❌ कोई default content मत दिखाओ

root.mainloop()
