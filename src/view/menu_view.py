from tkinter import *

from src.view.base_view import *
from src.controller.game_controller import *
from src.controller.menu_controller import *

class MenuView(BaseView):
    new_game_button = None

    def __init__(self, root):
        super().__init__(root)

        self.new_game_button = Button(self.canvas, command=self.new_game, text="Nieuw Spel")
        self.new_game_button.pack(side=CENTER)
    
    def new_game(self):
        game = GameController()
        game.reset()

        menu = MenuController()
        menu.to_page(GAME_VIEW)
