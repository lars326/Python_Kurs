import tkinter as tk

class SketchApp:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.last_x = None
        self.last_y = None

        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)

    def start_draw(self, event):
        self.last_x = event.x
        self.last_y = event.y

    def draw(self, event):
        x, y = event.x, event.y
        self.canvas.create_line(
            self.last_x, self.last_y, x, y,
            fill="black", width=2
        )
        self.last_x = x
        self.last_y = y


root = tk.Tk()
app = SketchApp(root)
root.mainloop()