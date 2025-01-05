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
                     is made outside of it, default popup type
        """

        tk.Toplevel.__init__(self, root)
        if size_x > rw or size_y > rh :
            raise Exception("Popup : popup is bigger then root window.")

        geometry = str(size_x) + "x" + str(size_y) + "+"
        # place the popup to the left if not enough place to the right
        self.x = x - size_x if (x + size_x) > rw else x
        # place the popup above if not enough place bellow
        self.y = y - size_y if (y + size_y) > rh else y

        

        geometry = geometry + str(self.x) + "+" + str(self.y)#position a avoir de la popup

        self.geometry(geometry)

        self.overrideredirect(True)
        self.withdraw()

        im = Image.open(disp.CANCEL)
        self.cancel = ImageTk.PhotoImage(im)

        self.exit_button = tk.Button(self, image=self.cancel,
            height = 30, width = 30, command = self.destroy)

        self.exit_button.pack(side=tk.TOP, anchor = tk.NE)

        self.drag = False

        #self.bind("<Leave>", self.switch_focus)
        #self.bind("<Enter>", self.switch_focus)
        self.mpos = (0, 0)

        self.bind("<1>", self.click)
        self.bind("<ButtonRelease-1>", self.drop)
        self.bind("<B1-Motion>", self.move)



    def natural_tile(self, type, ressources, territory):
        """
        ephemeral
        displays the type, territory it belongs to, and ressources of the tile.
        it has a button opening a vassal / stranger / enemy popup if it corresponds
        """
        titre = tk.Label(self, text= type)
        titre.pack(side=tk.TOP)
        tertext = "territory: " + territory
        titre = tk.Label(self, text= tertext)
        titre.pack(side=tk.TOP)
        self.show()

    def buildable_tile(self, x, y, type, territory, ressources ):
        pass

    def village_tile(self, x, y, territory):
        titre = tk.Label(self, text="village")
        titre.pack(side=tk.TOP)
        tertext = "territory: " + territory
        titre = tk.Label(self, text= tertext)
        titre.pack(side=tk.TOP)
        self.show()

    def ressources_popup(root, rx, rh, x, y, type, prod, quantity):
        pass

    def show(self):
        self.deiconify()

    def hide(self):
        self.withdraw()
    
    def drop(self, e):
        self.drag = False

    def click(self, e):
        self.drag = True
        self.mpos = (e.x, e.y)
    
    def move(self, e):
        if self.drag:
            x,y = self.x, self.y
            self.x = self.x + e.x - self.mpos[0]
            self.y = self.y + e.y - self.mpos[1]
            geometry = "+" + str(self.x) + "+" + str(self.y)
            self.geometry(geometry)



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
