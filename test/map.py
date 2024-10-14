import tkinter as tk
from PIL import Image, ImageTk
import random as rand

mat = [ [rand.randint(0,3) for i in range(40)] for j in range(40) ]

root = tk.Tk()

canv = tk.Canvas(root, width = 4000, height = 4000, bg='grey')
canv.configure(scrollregion=(0, 0, 4000, 4000))
canv.pack()

x,y = 0, 0
size = 100

texture = ['green', 'blue', 'grey', 'purple']

for line in mat:
    for tile in line:
        canv.create_rectangle(x, y, x+size, y+size, fill=texture[tile])
        y+=100
    x+=100
    y = 0

xpos,ypos = 0,0

startpos = (0,0)

def scroll_start(e):
    x,y = e.x, e.y
    canv.scan_mark(xpos,ypos)

def scroll_end(e):
    x,y = e.x, e.y
    canv.scan_dragto(x, y)


canv.bind("<ButtonPress-1>", scroll_start)
canv.bind("<B1-Motion>", scroll_end)

root.mainloop()

