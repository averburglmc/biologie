import random

from src.data import *
from src.pages.base_page import *
from src.models.enemy import *
from src.models.frog import *
from tkinter import *

class GamePage(BaseFrame):
    input = None
    chromosome = None

    _enemies = []
    _hearts = []

    paused = True

    def __init__(self, root, controller, input, chromosome):
        super().__init__(root, controller)

        self.input = input
        self.chromosome = chromosome

        controller.add_health_listener(self.lose_health)

    def reset(self, root, controller, input, chromosome):
        self.paused = False
        max_health = math.ceil(chromosome.get(HEALTH).locus / 10)
        for i in range(max_health):
            x_pos = -((max_health - 1) / 2) + i
            self._hearts.append(Sprite(self.canvas, controller, 400 + x_pos * 48, 32, 0, HEART_DATA
            ))

        print(self._hearts)

        self.background = PhotoImage(file="src/images/instructions.png")
        self.canvas.create_image(400, 300, image=self.background, anchor=CENTER)

        self.spawn_frog(root, controller, input, chromosome)
        self.spawn_enemy_continuous(root, 800, 504, 2 + 0.1 * self.controller.level, FLY_DATA, 4000 - 100 * self.controller.level)
        self.spawn_enemy_continuous(root, 800, 464, 3 + 0.2 * self.controller.level, BIRD_DATA, 6000 - 150 * self.controller.level)

    def clear(self):
        self.paused = True
        self.canvas.delete("all")
        self._enemies = []
        self._hearts = []

    def spawn_frog(self, root, controller, input, chromosome):
        self.frog = Frog(self, root, self.canvas, controller, input, chromosome, 300, FROG_DATA)

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
            self.spawn_enemy(800, 550, 2.5, LOVE_DATA)
