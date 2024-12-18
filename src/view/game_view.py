import random

from tkinter import *

from src.controller.chromosome_controller import *
from src.controller.stat_controller import *
from src.data.animation_data import *
from src.model.enemy import *
from src.model.player import *
from src.model.sprite import *
from src.view.base_view import *

class GameView(BaseView):
    actors = {}
    hearts = []

    session_id = ""

    def __init__(self, root):
        super().__init__(root)

        stat = StatController()
        stat.add_health_listener(self.on_health)

    def reset(self, root):
        self.session_id = str(random.random())

        chromosome = ChromosomeController()
        max_health_value = chromosome.get_value(HEALTH)
        max_health = math.ceil(max_health_value / 10)

        stat = StatController()
        stat.reset(max_health)

        for i in range(max_health):
            x_pos = -((max_health - 1) / 2) + i
            self._hearts.append(Sprite(self.canvas, 400 + x_pos * 48, 32, "img/heart-0", "img/heart-1"))

        self.background = PhotoImage(file="img/instructions.png")
        self.canvas.create_image(400, 300, image=self.background, anchor=CENTER)

        self.spawn_frog(root)
        self.spawn_enemy_continuous(root, 800, 504, 2 + 0.1 * self.controller.level, FLY_DATA, 4000 - 100 * self.controller.level)
        self.spawn_enemy_continuous(root, 800, 464, 3 + 0.2 * self.controller.level, BIRD_DATA, 6000 - 150 * self.controller.level)

    def clear(self):
        self.session_id = ""
        self.canvas.delete("all")
        self._enemies = []
        self._hearts = []

    def spawn_frog(self, root, controller, input, chromosome):
        self.frog = Player(self, root, self.canvas, controller, input, chromosome, 300, FROG_DATA)

    def try_destroy_enemy(self, id, points):
        for enemy in self._enemies:
            if enemy.id == id:
                if (enemy.name != "love"):
                    self.add_points(points)
                    enemy.destroy(points)
                return enemy.name

    def destroy_enemy(self, id, points):
        for enemy in self._enemies:
            if enemy.id == id:
                if enemy.name == "love":
                    self.controller.to_page(2)
                else:
                    self.add_points(points)
                    enemy.destroy(points)
                return enemy.name

    def spawn_enemy_continuous(self, root, max_x, max_y, speed, data, cooldown):
        if self.paused:
            return

        self.spawn_enemy(max_x, max_y, speed, data)
        root.after(cooldown, self.spawn_enemy_continuous, root, max_x, max_y, speed, data, cooldown)

    def spawn_enemy(self, max_x, max_y, speed, data):
        random_y = max_y * random.random()
        self._enemies.append(
            Enemy(self.canvas, self.controller, max_x, random_y, speed, data)
        )

    def lose_health(self, health):
        if self.paused:
            return

        self._hearts[health].play_forever("empty")      

    def add_points(self, points):
        self.controller.points += points
        if self.controller.points > 3 * (self.controller.level + 1):
            self.controller.points = 0
            self.spawn_enemy(800, 550, 2.5, FRIEND_DATA)
