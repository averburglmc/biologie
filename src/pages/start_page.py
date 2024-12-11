from tkinter import *

from src.pages.base_page import *

class StartPage(BaseFrame):
    def __init__(self, root, controller):
        super().__init__(root, controller)
        self.controller = controller

        self._new_button = Button(self.canvas, command=self.start_game ,text="New game")
        self._new_button.pack(pady=100, side=BOTTOM)
    
    def start_game(self):
        self.controller.new()
        self.controller.to_page(1)
