from tkinter import *

from src.pages.dna_page import *
from src.pages.game_page import *
from src.pages.start_page import *

class View:
    _page = 0
    _pages = []

    root = None
    controller = None
    input = None
    chromosome = None

    def __init__(self, root, controller, input, chromosome):
        self.root = root
        self.controller = controller
        self.input = input
        self.chromosome = chromosome

        controller.add_page_listener(self.on_page)
        self.init_pages(root, controller, input, chromosome)

    def init_pages(self, root, controller, input, chromosome):
        self._pages.append(StartPage(root, controller))
        self._pages.append(GamePage(root, controller, input, chromosome))
        self._pages.append(DnaPage(root, controller, chromosome))
        self._pages[self._page].show()

    def on_page(self, page):
        self._pages[self._page].hide()
        self._page = page

        if self._page == 1:
            self._pages[1].reset(self.root, self.controller, self.input, self.chromosome)
        else:
            self._pages[1].clear()

        if self._page == 2:
            self._pages[2].reset()

        self._pages[self._page].show()