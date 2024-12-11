from src.settings import *
from tkinter import *

class BaseFrame:
    root = None
    controller = None
    canvas = None

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.create_canvas()

    def create_canvas(self):
        self.canvas = Canvas(self.root, background=SCREEN_COLOR, height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
        self.canvas.pack_propagate(False)

    def show(self):
        self.canvas.pack()

    def hide(self):
        self.canvas.pack_forget()