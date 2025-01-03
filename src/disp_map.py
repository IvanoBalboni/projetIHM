import tkinter as tk
from PIL import Image, ImageTk
import os

import disp_popup_factory as dpop
import player_factory as pf
import map as mp

PLAYER   = 0
NEUTRAL  = 1
VASSAL   = 2
STRANGER = 3
ENEMY    = 4

class DMap(tk.Canvas):
    def __init__(self, root, map, player_factory):
        tk.Canvas.__init__(self, root, background="black")
        self.root = root

        self.map = map
        self.pf = player_factory

        self.scroll_x = 100 * self.map.width
        self.scroll_y = 100 * self.map.height
        self.configure(scrollregion=(0,0,self.scroll_x, self.scroll_y))

        self.pack(expand=True, fill = tk.BOTH, side = tk.BOTTOM)


        x, y = 0, 0
        size = 100
        texture = ['lawn green','forest green', 'blue', 'grey']

        village_pos = [self.map.village_dict[k][0] for k in self.map.village_dict.keys()]
        #print(village_pos)

        for line in self.map.tiles:
            for tile in line:
                if (x//size, y//size) in village_pos:
                    emp = self.create_rectangle(x, y, x+size, y+size, fill="red",
                                              tags= ("tile", "village"))
                else:
                    temp = self.create_rectangle(x, y, x+size, y+size, fill=texture[tile//4],
                                                tags= ("tile"))
                x+=size
            y+=size
            x = 0
        
        # move on the map with left click:
        self.pop = None
        self.bind("<ButtonPress-1>", self.scroll_start)
        self.bind("<B1-Motion>", self.scroll_move)
    
    
    def tileMenu(self, event):
        if self.pop is not None:
            self.pop.destroy()
        id = self.find_withtag("current")
        print(self.root.winfo_width(),self.root.winfo_height())
        tags = self.gettags("current")
        if "tile" in tags:
            if "village" in tags:
                self.pop = dpop.Popup(self.root, self.root.winfo_width(), self.root.winfo_height(),
                                event.x, event.y, 200, 300)
                self.pop.village_tile(1,2,3)
            else:
                self.pop = dpop.Popup(self.root, self.root.winfo_width(), self.root.winfo_height(),
                                event.x, event.y, 200, 300)
                self.pop.natural_tile(1,2,3,4,5)
            self.pop.bind("<FocusOut>", self.pop.quit)
                
    
    def scroll_start(self, event):
        if self.pop is not None:
            self.pop.destroy()
        self.scan_mark(event.x, event.y)

    def scroll_move(self, event):
        self.scan_dragto(event.x, event.y, gain=1)

if __name__ == "__main__":
    pass