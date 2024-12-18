from tkinter import *

from src.controller import *
from src.controller.input_controller import *
from src.view.main_view import *

root = Tk()

chromosome = ChromosomeController()
controller = GameController(root, chromosome)
input = InputController(root, controller)
view = MainView(root, controller, input, chromosome)

mainloop()
