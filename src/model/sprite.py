from tkinter import *

class Sprite:
    canvas = None
    id = None
    image = None
    alt_image = None

    def __init__(self, canvas, x, y, image_path, alt_image_path):
        self.canvas = canvas
        self.image = PhotoImage(file=image_path)
        self.alt_image = PhotoImage(file=alt_image_path)
        self.id = canvas.create_image(x, y, image=self.image)

    def show_image(self):
        self.canvas.itemconfig(self.id, image=self.image)

    def show_alt_image(self):
        self.canvas.itemconfig(self.id, image=self.alt_image)