import random

from src.settings import *
from src.models.locus import *

class Chromosome:
    loci = []

    def __init__(self):
        self.reset()

    def reset(self):
        self.loci = []
        self.loci.append(Locus(init=INIT_SPEED, name=SPEED, desc=SPEED_DESC, color="#EEBBBB", chromosome=self))
        self.loci.append(Locus(init=INIT_HEALTH, name=HEALTH, desc=HEALTH_DESC, color="#BBEEBB", chromosome=self))
        self.loci.append(Locus(init=INIT_INTELLECT, name=INTELLECT, desc=INTELLECT_DESC, color="#BBBBEE", chromosome=self))
        self.loci.append(Locus(init=INIT_COURAGE, name=COURAGE, desc=COURAGE_DESC, color="#EEEEBB", chromosome=self))

    def get(self, name):
        for locus in self.loci:
            if locus.name == name:
                return locus

    def get_random(self):
        locus = random.choice(self.loci)
        locus.randomize()
        return locus