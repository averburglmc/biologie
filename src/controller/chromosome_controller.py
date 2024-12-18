import random

from src.settings import *

from src.controller.singleton import *
from src.data.locus_data import *
from src.model.locus import *

class ChromosomeController(Singleton):
    loci = {}

    def __init__(self):
        self.reset()

    def reset(self):
        self.loci = {}
        for key in LOCUS_DATA.keys():
            self.loci[key] = Locus(LOCUS_DATA[key])

    def get(self, name):
        return self.loci[name]

    def get_value(self, name):
        return self.loci[name].locus

    def get_random(self):
        keys = self.loci.keys()
        key = random.choice(keys)
        locus = self.loci[key]
        locus.randomize()
        return locus