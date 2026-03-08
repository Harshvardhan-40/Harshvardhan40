import tkinter as tk

def show_content(category):
    # पहले सभी पेजों को छिपा दें
    for frame in all_pages.values():
        frame.pack_forget()
    
    # चुने हुए कैटेगरी का पेज दिखाएँ
    all_pages[category].pack(fill='both', expand=True)

root = tk.Tk()
root.geometry("400x300")
root.title("Category Selector Example")

# --- टॉप पर category बटन ---
categories = ["Action", "Gaming", "Education"]

for cat in categories:
    btn = tk.Button(root, text=cat, width=10, command=lambda c=cat: show_content(c))
    btn.pack(side="top", pady=5)

# --- अलग-अलग पेज बनाएँ ---
all_pages = {}

# Action page
action_frame = tk.Frame(root, bg="lightblue")
tk.Label(action_frame, text="🎬 Action से संबंधित कंटेंट", font=("Arial", 14), bg="lightblue").pack()
all_pages["Action"] = action_frame

# Gaming page
gaming_frame = tk.Frame(root, bg="lightgreen")
tk.Label(gaming_frame, text="🎮 Gaming से संबंधित कंटेंट", font=("Arial", 14), bg="lightgreen").pack(pady=30)
all_pages["Gaming"] = gaming_frame

# Education page
edu_frame = tk.Frame(root, bg="lightyellow")
tk.Label(edu_frame, text="📚 Education से संबंधित कंटेंट", font=("Arial", 14), bg="lightyellow").pack(pady=30)
all_pages["Education"] = edu_frame

# Default: कुछ न दिखाएँ
# आप चाहें तो कोई default दिखा सकते हैं
# show_content("Gaming")  # Example: Gaming default

root.mainloop()
