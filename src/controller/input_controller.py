from tkinter import *
from src.settings import *

class InputController:
    keys_pressed = []
    on_key = {}
    on_space = []

    def __init__(self, root, controller):
        controller.add_update_listener(self.update, True)

        root.bind("<KeyPress>", self.on_key_press)
        root.bind("<KeyRelease>", self.on_key_release)
        root.bind("<space>", self.on_space_key)

    def on_key_press(self, event):
        if not event.char in self.keys_pressed:
            self.keys_pressed.append(event.char)

    def on_key_release(self, event):
        if event.char in self.keys_pressed:
            self.keys_pressed.remove(event.char)

    def update(self):
        for key in self.keys_pressed:
            for listener in self.on_key[key]:
                listener()

    def on_space_key(self, _):
        for listener in self.on_space:
            listener()

    def add_key_listener(self, key, listener):
        if not key in self.on_key:
            self.on_key[key] = []
        self.on_key[key].append(listener)

    def add_space_listener(self, listener):
        self.on_space.append(listener)