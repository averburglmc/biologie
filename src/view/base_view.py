from src.settings import *
from tkinter import *

class BaseView:
    canvas = None

    def __init__(self, root):
        self.canvas = Canvas(root, background=SCREEN_COLOR, height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
        self.canvas.pack_propagate(False)

    def show(self):
        self.canvas.pack()

    def hide(self):
        self.canvas.pack_forget()