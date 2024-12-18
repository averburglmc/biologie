import math

from src.settings import *

from src.controller.menu_controller import *
from src.controller.singleton import *

class GameController(Singleton):
    on_draw = []
    on_update = []

    points = 0
    level = 0

    def __init__(self, root):
        self.draw(root)
        self.update(root)

        menu = MenuController()
        menu.add_page_listener(self.on_page)

    def new(self):
        self.level = 0

    def reset(self):
        self.points = 0
        self.health = math.ceil(self.chromosome.get(HEALTH).locus / 10)

    def add_draw_listener(self, listener, important):
        self.on_draw.append({
            "important": important,
            "listener": listener,
        })

    def add_update_listener(self, listener, important):
        self.on_update.append({
            "important": important,
            "listener": listener,
        })

    def remove_update_listener(self, listener):
        for l in self.on_update:
            if l == listener:
                self.on_update.remove(l)

    def draw(self, root):
        self.fire_draw()
        root.after(200, self.draw, root)

    def update(self, root):
        if self.page == 1:
            self.fire_update()
        root.after(10, self.update, root)

    def fire_draw(self):
        for listener in self.on_draw:
            listener["listener"]()

    def fire_update(self):
        for listener in self.on_update:
            listener["listener"]()

    def on_page(self, page):
        if page is GAME_VIEW:
            self.reset()
        else:
            self.clear_listeners()

    def add_points(self, points):
        self.points += points
    
    def clear_listeners(self):
        for draw_listener in self.on_draw:
            if not draw_listener["important"]:
                self.on_draw.remove(draw_listener)
        
        for update_listener in self.on_update:
            if not update_listener["important"]:
                self.on_update.remove(update_listener)

        for draw_listener in self.on_draw:
            if not draw_listener["important"]:
                self.on_draw.remove(draw_listener)
        
        for update_listener in self.on_update:
            if not update_listener["important"]:
                self.on_update.remove(update_listener)