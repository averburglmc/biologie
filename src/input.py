from tkinter import *

UP_KEY = "w"
DOWN_KEY = "s"
LEFT_KEY = "a"
RIGHT_KEY = "d"

class Input:
    _on_up = []
    _on_down = []
    _on_space = []
    _on_left = []
    _on_right = []

    _going_up = False
    _going_down = False
    _going_left = False
    _going_right = False
    
    def __init__(self, root, controller):
        controller.add_update_listener(self.update, True)

        root.bind("<KeyPress>", self.on_key_press)
        root.bind("<KeyRelease>", self.on_key_release)
        root.bind("<space>", self.on_space_key)

    def on_key_press(self, event):
        if event.char == UP_KEY:
            self._going_up = True
        if event.char == DOWN_KEY:
            self._going_down = True
        if event.char == LEFT_KEY:
            self._going_left = True
        if event.char == RIGHT_KEY:
            self._going_right = True

    def on_key_release(self, event):
        if event.char == UP_KEY:
            self._going_up = False
        if event.char == DOWN_KEY:
            self._going_down = False
        if event.char == LEFT_KEY:
            self._going_left = False
        if event.char == RIGHT_KEY:
            self._going_right = False

    def update(self):
        if self._going_up:
            self.fire_up()
        if self._going_down:
            self.fire_down()
        if self._going_left:
            self.fire_left()
        if self._going_right:
            self.fire_right()

    def on_space_key(self, event):
        self.fire_space()

    def fire_up(self):
        for listener in self._on_up:
            listener()

    def fire_down(self):
        for listener in self._on_down:
            listener()

    def fire_left(self):
        for listener in self._on_left:
            listener()

    def fire_right(self):
        for listener in self._on_right:
            listener()

    def fire_space(self):
        for listener in self._on_space:
            listener()

    def add_up_listener(self, listener):
        self._on_up.append(listener)

    def add_down_listener(self, listener):
        self._on_down.append(listener)

    def add_space_listener(self, listener):
        self._on_space.append(listener)

    def add_left_listener(self, listener):
        self._on_left.append(listener)
    
    def add_right_listener(self, listener):
        self._on_right.append(listener)