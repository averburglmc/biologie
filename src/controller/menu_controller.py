from src.settings import *

from src.controller.singleton import *

class MenuController(Singleton):
    on_page = []

    page = MENU_VIEW

    def add_page_listener(self, listener):
        self.on_page.append(listener)

    def to_page(self, new_page):
        for listener in self.on_page:
            listener(self.page, new_page)
        self.page = new_page