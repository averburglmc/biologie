from tkinter import *

class LocusFrame:
    index = 0

    def __init__(self, root, index):
        self.index = index

        self._frame = Frame(root)
        self._frame.pack()