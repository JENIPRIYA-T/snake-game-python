from tkinter import *
import random

w = Tk()
w.title("Snake Game")
canvas = Canvas(w, width=400, height=400, bg="black")
canvas.pack()
score = Label(w, text="Score: 0", font=("Arial", 14))
score.pack()

snake, dir, pts = [(100, 100)], "Right", 0
food = canvas.create_oval(200, 200, 220, 220, fill="red")

def reset():
    global snake, dir, pts
    snake, dir, pts = [(100, 100)], "Right", 0
    score.config(text="Score: 0")
    canvas.delete("all")
    spawn_food()
    move()

def spawn_food():
    global food
    x, y = random.randint(0, 19)*20, random.randint(0, 19)*20
    food = canvas.create_oval(x, y, x+20, y+20, fill="red", tag="food")

def move():
    global snake, pts
    x, y = snake[0]
    if dir == "Up": y -= 20
    if dir == "Down": y += 20
    if dir == "Left": x -= 20
    if dir == "Right": x += 20
    new = (x, y)
    if x < 0 or x >= 400 or y < 0 or y >= 400 or new in snake:
        canvas.create_text(200, 200, text="Game Over", fill="white", font=("", 24))
        return
    snake = [new] + snake
    if canvas.coords(food)[:2] == [x, y]:
        pts += 1
        score.config(text=f"Score: {pts}")
        canvas.delete("food")
        spawn_food()
    else:
        snake.pop()
    canvas.delete("snake")
    for s in snake:
        canvas.create_rectangle(s[0], s[1], s[0]+20, s[1]+20, fill="lime", tag="snake")
    w.after(100, move)

def change(e):
    global dir
    d = e.keysym
    if (dir, d) not in [("Up", "Down"), ("Down", "Up"), ("Left", "Right"), ("Right", "Left")]:
        dir = d

Button(w, text="Reset", command=reset).pack()
w.bind("<Key>", change)
move()
w.mainloop()

