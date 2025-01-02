import tkinter as tk
from PIL import Image, ImageTk
import os

import disp_header as disp
import disp_map    as dmap
import game

class Scene(tk.Frame):
    def __init__(self, root, game):
        tk.Frame.__init__(self, root)
        #self.menucanvas = tk.Canvas(self, background="grey")

        self.root = root

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.configure(height = self.screen_height, width = self.screen_width)

        self.game = game

        self.dmap  = dmap.DMap(self.root, self.game.map)



if __name__ == "__main__":
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    g = game.Game("save")
    Scene(root, g).pack(fill="both", expand=True)
    root.mainloop()