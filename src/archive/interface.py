from tkinter import *
from tile import *

import random

height = 20
width = 30

tiles = [[Tile(color='#EEEECC', type='none') for x in range(width)] for y in range(height)]
prey = [Tile(color='#888866', type='prey') for i in range(10)]

root = Tk()

def spawn():
    for i in range(10):
        animal = prey[i]
        animal.x = random.randint(0, width - 1)
        animal.y = random.randint(0, height - 1)
        tiles[animal.y][animal.x] = animal

def iterate(event):
    for p in prey:
        tiles[p.y][p.x] = Tile(color='#EEEECC', type='none')
        p.x += 1
        p.x = p.x % width
        tiles[p.y][p.x] = p
    draw()

root.bind("<space>", iterate)

def draw():
    for x in range(width):
        for y in range(height):
            Entry(root, bg=tiles[y][x].color, font='Arial 12', width=2).grid(row=y, column=x)
    
spawn()
draw()
mainloop()