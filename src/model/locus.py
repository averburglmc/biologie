import random
import math

class Locus:
    color = ""
    desc = ""
    name = ""

    allel_a = 0
    allel_b = 0
    init = 0
    locus = 0

    def __init__(self, data):
        self.color = data["color"]
        self.desc = desc
        self.name = name
        self.init = init
        self.reset()

    def reset(self):
        self.allel_a = self.init
        self.allel_b = self.init
        self.locus = self.init
        self.reset_code()

    def reset_code(self):
        self.code = "self.locus=self.allel_a"

    def run(self):
        try:
            exec(self.code)
            return True
        except:
            self.reset_code()
            return False

    def randomize(self):
        self.allel_a = self.locus
        self.allel_b = self.locus

        i = 10
        while i > 0 and self.allel_a == self.allel_b:
            adjustment = 0.5 + random.random()
            self.allel_b = math.floor(self.locus * adjustment)
            i -= 1