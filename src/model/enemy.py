from src.model.animated_sprite import *

class Enemy(AnimatedSprite):
    def __init__(self, canvas, controller, x, y, speed, data):
        super().__init__(canvas, controller, x, y, speed, data)
        self.controller.add_update_listener(self.update, False)

    def destroy(self, points):
        self.controller.remove_update_listener(self.update)
        self.controller.add_points(points)
        self.canvas.delete(self.id)

    def update(self):
        self.x -= self.speed
        if self.x < -200:
            self.destroy(0)
        else:
            self.move()
    
    def move(self):
        self.canvas.moveto(self.id, self.x, self.y)
        