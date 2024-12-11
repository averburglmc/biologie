import math

from src.settings import *

class Controller:
    chromosome = None

    on_draw = []
    on_health = []
    on_page = []
    on_update = []

    points = 0
    page = 0
    health = 0
    level = 0

    def __init__(self, root, chromosome):
        self.chromosome = chromosome
        self.draw(root)
        self.update(root)

    def new(self):
        self.level = 0

    def reset(self):
        self.points = 0
        self.health = math.ceil(self.chromosome.get(HEALTH).locus / 10)

    def add_page_listener(self, listener):
        self.on_page.append(listener)

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

    def add_health_listener(self, listener):
        self.on_health.append(listener)

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

    def fire_page(self, page):
        for listener in self.on_page:
            listener(page)

    def fire_draw(self):
        for listener in self.on_draw:
            listener["listener"]()

    def fire_update(self):
        for listener in self.on_update:
            listener["listener"]()

    def fire_health(self, health):
        for listener in self.on_health:
            listener(health)

    def to_page(self, page):
        self.page = page

        if self.page != 1:
            self.clear_listeners()
        else:
            self.reset()

        self.fire_page(page)

    def add_points(self, points):
        self.points += points
    
    def lose_health(self):
        self.health -= 1
        if self.health == 0:
            self.to_page(0)
        else:
            self.fire_health(self.health)

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
