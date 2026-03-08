import tkinter as tk
from tkinter import messagebox, simpledialog

class SocialMediaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Instagram")
        self.root.geometry("600x600")
        self.root.config(bg="white")

        # Fake users
        self.users = {"admin": "123"}
        self.current_user = None

        # Posts (list of dicts)
        self.posts = [
            {"user": "admin", "text": "Welcome to Mini Instagram!", "likes": 0, "comments": []}
        ]

        self.login_page()

    # -------- LOGIN PAGE --------
    def login_page(self):
        self.clear()
        tk.Label(self.root, text="Mini Instagram", font=("Arial", 24, "bold"), bg="white", fg="#262626").pack(pady=30)

        tk.Label(self.root, text="Username:", bg="white").pack()
        self.username_entry = tk.Entry(self.root, width=30)
        self.username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:", bg="white").pack()
        self.password_entry = tk.Entry(self.root, width=30, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.root, text="Login", bg="#0095F6", fg="white", width=20, command=self.login).pack(pady=15)
        tk.Button(self.root, text="Sign Up", bg="white", fg="#0095F6", command=self.signup).pack()

    def login(self):
        user = self.username_entry.get()
        pwd = self.password_entry.get()
        if user in self.users and self.users[user] == pwd:
            self.current_user = user
            self.home_page()
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

    def signup(self):
        user = self.username_entry.get()
        pwd = self.password_entry.get()
        if user in self.users:
            messagebox.showerror("Error", "User already exists!")
        else:
            self.users[user] = pwd
            messagebox.showinfo("Success", "Account created! Now login.")

    # -------- HOME PAGE --------
    def home_page(self):
        self.clear()
        tk.Label(self.root, text=f"Welcome, {self.current_user}", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

        # Post Area
        self.post_frame = tk.Frame(self.root, bg="white")
        self.post_frame.pack(fill="both", expand=True)

        self.show_posts()

        # Add Post
        tk.Label(self.root, text="Write a new post:", bg="white").pack(pady=5)
        self.new_post_entry = tk.Entry(self.root, width=40)
        self.new_post_entry.pack(pady=5)
        tk.Button(self.root, text="Post", bg="#0095F6", fg="white", command=self.add_post).pack(pady=5)

        tk.Button(self.root, text="Logout", command=self.login_page).pack(pady=10)

    def show_posts(self):
        for widget in self.post_frame.winfo_children():
            widget.destroy()

        for idx, post in enumerate(self.posts):
            frame = tk.Frame(self.post_frame, bd=1, relief="solid", padx=10, pady=5, bg="white")
            frame.pack(fill="x", pady=5)

            tk.Label(frame, text=f"{post['user']}", font=("Arial", 10, "bold"), bg="white").pack(anchor="w")
            tk.Label(frame, text=post["text"], bg="white").pack(anchor="w", pady=2)

            like_btn = tk.Button(frame, text=f"❤️ {post['likes']}", bg="white", bd=0,
                                 command=lambda i=idx: self.like_post(i))
            like_btn.pack(side="left", padx=5)

            comment_btn = tk.Button(frame, text="💬 Comment", bg="white", bd=0,
                                    command=lambda i=idx: self.comment_post(i))
            comment_btn.pack(side="left", padx=5)

            # Show comments
            if post["comments"]:
                tk.Label(frame, text="Comments:", font=("Arial", 9, "bold"), bg="white").pack(anchor="w")
                for c in post["comments"]:
                    tk.Label(frame, text=f"- {c}", bg="white", fg="grey").pack(anchor="w")

    def add_post(self):
        text = self.new_post_entry.get()
        if text.strip():
            self.posts.insert(0, {"user": self.current_user, "text": text, "likes": 0, "comments": []})
            self.new_post_entry.delete(0, tk.END)
            self.show_posts()

    def like_post(self, idx):
        self.posts[idx]["likes"] += 1
        self.show_posts()

    def comment_post(self, idx):
        comment = simpledialog.askstring("Comment", "Write your comment:")
        if comment:
            self.posts[idx]["comments"].append(f"{self.current_user}: {comment}")
            self.show_posts()

    # -------- CLEAR WINDOW --------
    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# -------- RUN APP --------
if __name__ == "__main__":
    root = tk.Tk()
    app = SocialMediaApp(root)
    root.mainloop()
