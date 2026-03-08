import tkinter as tk
from tkinter import messagebox, simpledialog

class MiniInstagram:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Instagram")
        self.root.geometry("650x650")
        self.root.config(bg="white")

        # User data
        self.users = {"admin": "123"}
        self.user_bios = {"admin": "Hello! I am the first user."}
        self.current_user = None

        # Posts data
        self.posts = [
            {"user": "admin", "text": "Welcome to Mini Instagram!", "likes": 0, "comments": []}
        ]

        self.login_page()

    # ---------- LOGIN PAGE ----------
    def login_page(self):
        self.clear()
        tk.Label(self.root, text="Instagram", font=("Arial", 32, "bold"), bg="white", fg="#262626").pack(pady=40)

        tk.Label(self.root, text="Username", bg="white").pack()
        self.username_entry = tk.Entry(self.root, width=30)
        self.username_entry.pack(pady=5)

        tk.Label(self.root, text="Password", bg="white").pack()
        self.password_entry = tk.Entry(self.root, width=30, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.root, text="Log In", bg="#0095F6", fg="white", width=20, command=self.login).pack(pady=15)
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
            self.user_bios[user] = "New user. Add your bio!"
            messagebox.showinfo("Success", "Account created! Now login.")

    # ---------- HOME PAGE ----------
    def home_page(self):
        self.clear()
        tk.Label(self.root, text=f"Welcome, {self.current_user}", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

        # Navigation
        nav = tk.Frame(self.root, bg="white")
        nav.pack(pady=5)
        tk.Button(nav, text="🏠 Home", command=self.home_page, bg="white").pack(side="left", padx=10)
        tk.Button(nav, text="👤 Profile", command=self.profile_page, bg="white").pack(side="left", padx=10)
        tk.Button(nav, text="🔍 Explore", command=self.explore_page, bg="white").pack(side="left", padx=10)
        tk.Button(nav, text="🚪 Logout", command=self.login_page, bg="white").pack(side="left", padx=10)

        # Post Area
        self.post_frame = tk.Frame(self.root, bg="white")
        self.post_frame.pack(fill="both", expand=True)
        self.show_posts()

        # Add Post
        tk.Label(self.root, text="Write a new post:", bg="white").pack(pady=5)
        self.new_post_entry = tk.Entry(self.root, width=40)
        self.new_post_entry.pack(pady=5)
        tk.Button(self.root, text="Post", bg="#0095F6", fg="white", command=self.add_post).pack(pady=5)

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

    # ---------- PROFILE PAGE ----------
    def profile_page(self):
        self.clear()
        tk.Label(self.root, text=f"{self.current_user}'s Profile", font=("Arial", 18, "bold"), bg="white").pack(pady=10)

        bio = self.user_bios.get(self.current_user, "No bio yet.")
        self.bio_label = tk.Label(self.root, text=bio, bg="white", fg="grey", font=("Arial", 10))
        self.bio_label.pack(pady=5)

        tk.Button(self.root, text="✏️ Edit Bio", bg="white", command=self.edit_bio).pack(pady=5)

        tk.Label(self.root, text="Your Posts:", font=("Arial", 12, "bold"), bg="white").pack(pady=10)

        for post in self.posts:
            if post["user"] == self.current_user:
                frame = tk.Frame(self.root, bd=1, relief="solid", padx=10, pady=5, bg="white")
                frame.pack(fill="x", pady=5)
                tk.Label(frame, text=post["text"], bg="white").pack(anchor="w")

        nav = tk.Frame(self.root, bg="white")
        nav.pack(side="bottom", pady=10)
        tk.Button(nav, text="🏠 Home", command=self.home_page, bg="white").pack(side="left", padx=10)
        tk.Button(nav, text="🔍 Explore", command=self.explore_page, bg="white").pack(side="left", padx=10)
        tk.Button(nav, text="🚪 Logout", command=self.login_page, bg="white").pack(side="left", padx=10)

    def edit_bio(self):
        new_bio = simpledialog.askstring("Edit Bio", "Write your new bio:")
        if new_bio:
            self.user_bios[self.current_user] = new_bio
            self.profile_page()

    # ---------- EXPLORE PAGE ----------
    def explore_page(self):
        self.clear()
        tk.Label(self.root, text="Explore", font=("Arial", 18, "bold"), bg="white").pack(pady=10)

        for user in self.users:
            if user != self.current_user:
                frame = tk.Frame(self.root, bd=1, relief="solid", padx=10, pady=5, bg="white")
                frame.pack(fill="x", pady=5)

                tk.Label(frame, text=f"👤 {user}", font=("Arial", 12, "bold"), bg="white").pack(anchor="w")
                tk.Label(frame, text=self.user_bios.get(user, ""), bg="white", fg="grey").pack(anchor="w")

                tk.Label(frame, text="Posts:", bg="white", font=("Arial", 10, "bold")).pack(anchor="w")
                for post in self.posts:
                    if post["user"] == user:
                        tk.Label(frame, text=f"- {post['text']}", bg="white").pack(anchor="w")

        nav = tk.Frame(self.root, bg="white")
        nav.pack(side="bottom", pady=10)
        tk.Button(nav, text="🏠 Home", command=self.home_page, bg="white").pack(side="left", padx=10)
        tk.Button(nav, text="👤 Profile", command=self.profile_page, bg="white").pack(side="left", padx=10)
        tk.Button(nav, text="🚪 Logout", command=self.login_page, bg="white").pack(side="left", padx=10)

    # ---------- CLEAR WINDOW ----------
    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# ---------- RUN APP ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = MiniInstagram(root)
    root.mainloop()
