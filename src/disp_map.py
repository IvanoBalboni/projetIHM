import tkinter as tk
from PIL import Image, ImageTk
import os

class DMap(tk.Canvas):
    def __init__(self, root, map):
        tk.Canvas.__init__(self, root, background="black")

        self.map = map

        self.scroll_x = 100 * self.map.width
        self.scroll_y = 100 * self.map.height
        self.configure(scrollregion=(0,0,self.scroll_x, self.scroll_y))

        self.pack(expand=True, fill = tk.BOTH, side = tk.BOTTOM)


        x, y = 0, 0
        size = 100
        texture = ['lawn green','forest green', 'blue', 'grey']

        for line in self.map.tiles:
            for tile in line:
                self.create_rectangle(x, y, x+size, y+size, fill=texture[tile//4])
                x+=100
            y+=100
            x = 0
        
        # move on the map with left click:
        self.bind("<ButtonPress-1>", self.scroll_start)
        self.bind("<B1-Motion>", self.scroll_move)
    
    def scroll_start(self, event):
        self.scan_mark(event.x, event.y)

    def scroll_move(self, event):
        self.scan_dragto(event.x, event.y, gain=1)

if __name__ == "__main__":
    pass