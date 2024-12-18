from tkinter import *

from src.settings import *

from src.controller.menu_controller import *
from src.view.dna_view import *
from src.view.game_view import *
from src.view.menu_view import *

class MainView:
    views = {}

    def __init__(self, root):
        self.views[DNA_VIEW] = DnaView(root)
        self.views[GAME_VIEW] = GameView(root)
        self.views[MENU_VIEW] = MenuView(root)
        self.views[MENU_VIEW].show()

        menu = MenuController()
        menu.add_page_listener(self.on_page)

    def on_page(self, previous_page, new_page):
        self.views[previous_page].hide()
        self.views[new_page].show()