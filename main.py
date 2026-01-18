import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Графический редактор")

        self.brush_color = "black"
        self.brush_size = 5
        self.last_x, self.last_y = None, None

        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # кнопки
        button_frame = tk.Frame(root)
        button_frame.pack(fill=tk.X)

        tk.Button(button_frame, text="Цвет", command=self.choose_color).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Толщина +", command=self.increase_size).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Толщина -", command=self.decrease_size).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Стереть", command=self.erase).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Очистить", command=self.clear_canvas).pack(side=tk.LEFT, padx=5)

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_paint)

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.brush_color = color

    def increase_size(self):
        self.brush_size += 1

    def decrease_size(self):
        if self.brush_size > 1:
            self.brush_size -= 1

    def erase(self):
        self.brush_color = "white"

    def clear_canvas(self):
        self.canvas.delete("all")

    def on_button_press(self, event):
        self.last_x, self.last_y = event.x, event.y

    def on_paint(self, event):
        x, y = event.x, event.y
        if self.last_x and self.last_y:
            self.canvas.create_line(
                self.last_x, self.last_y, x, y,
                fill=self.brush_color,
                width=self.brush_size,
                capstyle=tk.ROUND,
                smooth=True
            )
        self.last_x, self.last_y = x, y


if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()