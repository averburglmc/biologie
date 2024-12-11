from tkinter import *

from src.chromosome import *
from src.controller import *
from src.input import *
from src.view import *

root = Tk()

chromosome = Chromosome()
controller = Controller(root, chromosome)
input = Input(root, controller)
view = View(root, controller, input, chromosome)

mainloop()
