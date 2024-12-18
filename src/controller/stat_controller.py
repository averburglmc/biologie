from src.controller.singleton import *

class StatController(Singleton):
    on_health = []

    health = 1
    max_health = 1

    def reset(self, max_health):
        self.max_health = max_health
        self.health = max_health

    def add_health_listener(self, listener):
        self.on_health.append(listener)

    def set_health(self, health):
        self.health = health
        for listener in self.on_health:
                listener(health)