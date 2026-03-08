import tkinter as tk
import random

class FreeFireDemo:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Free Fire - Tkinter Demo")
        self.root.geometry("600x400")

        # Canvas
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="black")
        self.canvas.pack()

        # Player
        self.player = self.canvas.create_rectangle(280, 350, 320, 380, fill="blue")

        # Enemy
        self.enemy = self.canvas.create_rectangle(280, 50, 320, 80, fill="red")

        # Bullets list
        self.bullets = []

        # Key bindings
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<space>", self.shoot)

        # Game loop
        self.update_game()

    def move_left(self, event):
        self.canvas.move(self.player, -20, 0)

    def move_right(self, event):
        self.canvas.move(self.player, 20, 0)

    def shoot(self, event):
        # Player coords
        x1, y1, x2, y2 = self.canvas.coords(self.player)
        bullet = self.canvas.create_rectangle((x1+x2)//2-2, y1-10, (x1+x2)//2+2, y1, fill="yellow")
        self.bullets.append(bullet)

    def update_game(self):
        # Move bullets
        for bullet in self.bullets[:]:
            self.canvas.move(bullet, 0, -10)
            bx1, by1, bx2, by2 = self.canvas.coords(bullet)
            ex1, ey1, ex2, ey2 = self.canvas.coords(self.enemy)

            # Check collision
            if bx1 < ex2 and bx2 > ex1 and by1 < ey2 and by2 > ey1:
                self.canvas.delete(self.enemy)
                self.canvas.delete(bullet)
                self.bullets.remove(bullet)
                self.enemy = self.canvas.create_rectangle(random.randint(50, 500), 50,
                                                          random.randint(100, 550), 80, fill="red")
            elif by2 < 0:  # Remove bullet if out of screen
                self.canvas.delete(bullet)
                self.bullets.remove(bullet)

        # Move enemy randomly
        dx = random.choice([-10, 0, 10])
        self.canvas.move(self.enemy, dx, 0)

        self.root.after(100, self.update_game)


# Run game
if __name__ == "__main__":
    root = tk.Tk()
    game = FreeFireDemo(root)
    root.mainloop()
