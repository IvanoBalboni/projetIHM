import tkinter as tk
from PIL import Image, ImageTk

import disp_header as disp

class Popup(tk.Toplevel):
    def __init__(self, root , rw, rh ,x, y, size_x, size_y):
        """
        opens a generic unmovable popup without borders
        it will adjust its position to always be visible (in our usecases)
        root           : window the popup must stay within
        rw,rh          : root width / height
        x, y           : mouse position / popup position
        size_x, size_y : popup size, it will always fit the root (in our usecases)
        3 types :
        lock       : the rest of the game can't be played
                     until actions on the popup are made
        persistant : the popup doesn't lock the game but will
                     stay displayed as long as it is needed
        ephemeral  : the popup will disapear the moment a click
                     is made outside of it
        """

        tk.Toplevel.__init__(self, root)
        if size_x > rw or size_y > rh :
            raise Exception("Popup : popup is bigger then root window.")

        geometry = str(size_x) + "x" + str(size_y) + "+"
        # place the popup to the left if not enough place to the right
        x = x - size_x if (x + size_x) > rw else x
        # place the popup above if not enough place bellow
        y = y - size_y if (y + size_y) > rw else y
        geometry = geometry + str(x) + "+" + str(y)

        self.geometry(geometry)

        self.overrideredirect(True)
        self.withdraw()

        im = Image.open(disp.CANCEL)
        self.cancel = ImageTk.PhotoImage(im)

        self.exit_button = tk.Button(self, image=self.cancel,
            height = 30, width = 30, command = self.destroy)

        self.exit_button.pack(side=tk.TOP, anchor = tk.NE)



    def natural_tile(self, x, y, type, territory, ressources):
        """
        ephemeral
        displays the type, territory it belongs to, and ressources of the tile.
        it has a button opening a vassal / stranger / enemy popup if it corresponds
        """
        pass

    def buildable_tile(self, x, y, type, territory, ressources, ):
        pass

    def village_tile(self, x, y, type, territory):
        pass

    def show(self):
        self.deiconify()

    def hide(self):
        self.withdraw()

    def ressources_popup(root, rx, rh, x, y, type, prod, quantity):
        pass

if __name__ == "__main__":
    def new_pop():
        pop = Popup(root, 500, 500, 425, 425, 100, 100)
        pop.show()

    root = tk.Tk()
    root.attributes("-fullscreen", True)
    stop = tk.Button(root, text = "exit", command = root.destroy)
    spawn = tk.Button(root, text = "spawn", command = new_pop)
    stop.pack()
    spawn.pack()
    root.geometry("500x500+0+0")
    root.mainloop()
