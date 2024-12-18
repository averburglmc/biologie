import time
from src.settings import *
from src.models.locus import *
from src.models.sprite import *

MAX_Y = 536
IDLE = "IDLE"
MOVE = "MOVE"
LICK = "LICK"
LICK2 = "LICK2"
HURT = "HURT"

class Frog(Sprite):
    state = IDLE

    def __init__(self, page, root, canvas, controller, input, chromosome, start_y, data):
        super().__init__(canvas, controller, 0, start_y, 2, data)
        self.page = page
        self.root = root
        self.chromosome = chromosome

        input.add_up_listener(self.up)
        input.add_down_listener(self.down)
        input.add_left_listener(self.left)
        input.add_right_listener(self.right)
        input.add_space_listener(self.lick)

        controller.add_update_listener(self.update, False)

    def up(self):
        if self.state == LICK or self.state == LICK2:
            return
        
        self.y -= self.chromosome.get(SPEED).locus / 10
        self.move()

    def down(self):
        if self.state == LICK or  self.state == LICK2:
            return
        
        self.y += self.chromosome.get(SPEED).locus / 10
        self.move()

    def left(self):
        if self.state == LICK or self.state == LICK2:
            return
        
        self.x -= self.chromosome.get(SPEED).locus / 10
        self.move()

    def right(self):
        if self.state == LICK or self.state == LICK2:
            return  
        
        self.x += self.chromosome.get(SPEED).locus / 10
        self.move()

    def move(self):
        self.state = MOVE

        if self.x > self.chromosome.get(COURAGE).locus:
            self.x = self.chromosome.get(COURAGE).locus
        if self.x < 0:
            self.x = 0

        if self.y > MAX_Y:
            self.y = MAX_Y
        if self.y < 0:
            self.y = 0

        self.canvas.moveto(self.id, self.x, self.y)

    def lick(self):
        if self.state == LICK or self.state == LICK2:
            return

        self.play("attack")
        self.state = LICK
        self.root.after(500, self.mid_lick)
        
    def mid_lick(self):
        self.state = LICK2
        self.root.after(250, self.end_lick)

    def end_lick(self):
        self.state = IDLE

    def update(self):
        coords = self.canvas.coords(self.id)

        if len(coords) < 2:
            return

        if self.state == LICK2:
            collisions = self.canvas.find_overlapping(coords[0], coords[1], coords[0] + 216, coords[1] + 12)
            if len(collisions) > 0 and collisions[-1] != self.id:
                name = self.page.try_destroy_enemy(collisions[-1], 1)
                if name == "bird":
                    self.hurt()
        else:
            collisions = self.canvas.find_overlapping(coords[0], coords[1], coords[0] + 64, coords[1] + 12)
            if len(collisions) > 0 and collisions[-1] != self.id:
                name = self.page.destroy_enemy(collisions[-1], 1)
                if name != "love":
                    self.hurt()
        
    def hurt(self):
        self.play("hurt")
        self.controller.lose_health()
