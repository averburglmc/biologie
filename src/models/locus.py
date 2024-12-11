import random
import math

class Locus:
    chromosome = None

    color = ""
    desc = ""
    name = ""

    allel_x = 0
    allel_y = 0
    init = 0
    locus = 0

    def __init__(self, name, desc, init, color, chromosome):
        self.chromosome = chromosome
        self.color = color
        self.desc = desc
        self.name = name
        self.init = init
        self.reset()

    def reset(self):
        self.allel_x = self.init
        self.allel_y = self.init
        self.locus = self.init
        self.reset_code()

    def reset_code(self):
        self.code = "self.locus=self.allel_x"

    def run(self):
        try:
            exec(self.code)
            return True
        except:
            self.reset_code()
            return False

    def randomize(self):
        self.allel_x = self.locus
        self.allel_y = self.locus

        i = 10
        while i > 0 and self.allel_x == self.allel_y:
            adjustment = 0.5 + random.random()
            self.allel_y = math.floor(self.locus * adjustment)
            i -= 1