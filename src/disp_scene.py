import tkinter as tk
from PIL import Image, ImageTk
import os

import disp_header as disp
import disp_map    as dmap
import disp_popup_factory as dp
import game

class Scene(tk.Frame):
    def __init__(self, root, game):
        tk.Frame.__init__(self, root)
        self.menucanvas = tk.Canvas(self, background="grey")
        self.root = root

        im = Image.open(disp.COIN)
        self.coin = ImageTk.PhotoImage(im)
        im = Image.open(disp.CANCEL)
        self.cancel = ImageTk.PhotoImage(im)
        im = Image.open(disp.FOOD)
        self.food = ImageTk.PhotoImage(im)
        im = Image.open(disp.WOOD)
        self.wood = ImageTk.PhotoImage(im)

        self.pop = dp.Popup(self, 2500, 1900, 50, 50, 100, 100)

        self.exit_button = tk.Button(self, image=self.cancel,
            height = 50, width = 50, command = self.root.destroy)
        
        self.money_button = tk.Button(self, text = "money", image=self.coin,
            height = 50, width = 150, compound="left", command = self.pop.show)
        
        self.food_button = tk.Button(self, text = "food", image=self.food,
            height = 50, width = 150, compound="left")
        self.wood_button = tk.Button(self, text = "wood", image=self.wood,
             height = 50, width = 150, compound="left")
        #self.screen_width = self.root.winfo_screenwidth()
        #self.screen_height = self.root.winfo_screenheight()
        #self.configure(height = self.screen_height, width = self.screen_width)

        self.game = game

        self.dmap  = dmap.DMap(self.root, self.game.map, self.game.pf)
        self.dmap.pack(expand=True, fill = tk.BOTH, side = tk.BOTTOM)

        self.money_button.pack(side=tk.LEFT)
        self.food_button.pack(side=tk.LEFT)
        self.wood_button.pack(side=tk.LEFT)
        self.exit_button.pack(side=tk.RIGHT)

        self.dmap.bind("<ButtonRelease-3>", self.dmap.tileMenu)



if __name__ == "__main__":
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    g = game.Game("save")
    Scene(root, g).pack()
    root.mainloop()