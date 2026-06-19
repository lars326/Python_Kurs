import tkinter as tk
import random

window = tk.Tk()
window.title("Racing Game")
window.geometry("400x600")

canvas = tk.Canvas(window, width=400, height=600, bg="gray")
canvas.pack()

# Auto
car = canvas.create_rectangle(180, 500, 220, 550, fill="blue")

# Strassenlinien
lines = []
for i in range(5):
    line = canvas.create_rectangle(195, i*120, 205, i*120+60, fill="white")
    lines.append(line)

# Hindernisse
obstacles = []

score = 0
speed = 6
game_over = False

score_text = canvas.create_text(70, 20, text="Score: 0", font=("Arial", 16))

# ---------------- Steuerung ----------------
def links(event=None):
    x1, y1, x2, y2 = canvas.coords(car)
    if x1 > 0:
        canvas.move(car, -20, 0)

def rechts(event=None):
    x1, y1, x2, y2 = canvas.coords(car)
    if x2 < 400:
        canvas.move(car, 20, 0)

# ---------------- Hindernisse ----------------
def spawn_obstacle():
    if game_over:
        return

    x = random.choice([80, 180, 280])
    obs = canvas.create_rectangle(x, -50, x+40, 0, fill="red")
    obstacles.append(obs)

    window.after(random.randint(800, 1500), spawn_obstacle)

# ---------------- Game Loop ----------------
def game_loop():
    global score, speed, game_over

    if game_over:
        return

    # Strassenlinien bewegen
    for line in lines:
        canvas.move(line, 0, speed)
        x1, y1, x2, y2 = canvas.coords(line)

        if y1 > 600:
            canvas.move(line, 0, -700)

    # Hindernisse bewegen
    for obs in obstacles:
        canvas.move(obs, 0, speed+2)

        ox1, oy1, ox2, oy2 = canvas.coords(obs)
        cx1, cy1, cx2, cy2 = canvas.coords(car)

        # Kollision
        if cx1 < ox2 and cx2 > ox1 and cy1 < oy2 and cy2 > oy1:
            game_over = True
            canvas.create_text(200, 300, text="CRASH!", font=("Arial", 30), fill="red")

    # Score
    score += 1
    canvas.itemconfig(score_text, text=f"Score: {score//10}")

    # Schwierigkeit
    if score % 200 == 0:
        speed += 1

    window.after(30, game_loop)

# Controls
window.bind("<Left>", links)
window.bind("<Right>", rechts)

spawn_obstacle()
game_loop()

window.mainloop()