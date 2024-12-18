from tkinter import *
from math import *

class AnimatedSprite:
    canvas = None
    controller = None
    data = None

    animations = {}

    base_anim = "idle"
    current_anim = "idle"
    name = ""

    current_frame = 0
    id = 0
    speed = 0
    x = 0
    y = 0

    def __init__(self, canvas, controller, x, y, speed, data):
        self.name = data["name"]

        self.canvas = canvas
        self.controller = controller
        self.data = data

        self.speed = speed
        self.x = x
        self.y = y

        self.init_animation()
        
        controller.add_draw_listener(self.draw, False)

        self.id = canvas.create_image(x, y, anchor=W, image=self.animations[self.current_anim][0])

    def init_animation(self):
        self.animations = {}
        self.current_anim = "idle"
        self.current_frame = 0

        for anim in self.data["animations"]:
            list = []
            for i in range(anim["frames"]):
                image_name = f"src/images/{self.data["name"]}-{anim["name"]}-{i}.png"
                image = PhotoImage(file=image_name)
                list.append(image)
            self.animations[anim["name"]] = list


    def draw(self):
        self.current_frame += 1
        if self.current_frame >= len(self.animations[self.current_anim]):
            self.current_anim = self.base_anim
            self.current_frame = 0
        
        self.canvas.itemconfig(self.id, image=self.animations[self.current_anim][self.current_frame])

    def update(self):
        pass
    
    def play(self, name):
        self.current_anim = name
        self.current_frame = -1
    
    def play_forever(self, name):
        self.base_anim = name
        self.play(name)