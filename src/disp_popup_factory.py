import tkinter as tk
from PIL import Image, ImageTk

import village as vil
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

        self.root = root

        tk.Toplevel.__init__(self, root)
        if size_x > rw or size_y > rh :
            raise Exception("Popup : popup is bigger then root window.")

        geometry = str(size_x) + "x" + str(size_y) + "+"
        # place the popup to the left if not enough place to the right
        self.x = x - size_x if (x + size_x) > rw else x
        # place the popup above if not enough place bellow
        self.y = y - size_y if (y + size_y) > rh else y

        self.size_x, self.size_y = size_x, size_y

        

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



    def natural_tile(self, type, pos, territory):
        """
        ephemeral
        displays the type, territory it belongs to, and ressources of the tile.
        it has a button opening a vassal / stranger / enemy popup if it corresponds
        """
        self.pos = pos
        titre = tk.Label(self, text= type)
        titre.pack(side=tk.TOP)
        tertext = "territory: " + territory
        titre = tk.Label(self, text= tertext)
        titre.pack(side=tk.TOP)

        self.bought = False
        if territory == "neutral" and not self.bought :
            self.acheter = tk.Button(self, text="buy", command = self.aquire)
            self.acheter.pack(side=tk.TOP)
        if territory == self.root.dmap.pf.players[self.root.dmap.current_player].name:
            self.acheter = tk.Button(self, text="construct", command = self.construct)
            self.acheter.pack(side=tk.TOP)

        self.show()
    
    def construct(self):
        self.root.dmap.construct(self.pos[0], self.pos[1])

    def aquire(self):
        self.root.dmap.aquire(self.pos[0], self.pos[1])

    def buildable_tile(self, x, y, type, pos, ressources ):
        pass

    def village_tile(self, village: vil.Village, pos, territory):
        self.pos = pos
        titre = tk.Label(self, text="village")
        titre.pack(side=tk.TOP)
        self.village = village

        tertext = "territory: " + territory
        titre = tk.Label(self, text= tertext)
        titre.pack(side=tk.TOP)

        tertext = "food: " + str(village.food) + " + " + str(village.food_multiplier)
        titre = tk.Label(self, text= tertext)
        titre.pack(side=tk.TOP) 

        tertext = "wood: " + str(village.wood) + " + " + str(village.wood_multiplier)
        titre = tk.Label(self, text= tertext)
        titre.pack(side=tk.TOP)

        self.villagers = tk.Button(self, text="update", command = village.update)
        self.villagers.pack(side=tk.TOP)

        self.villagers = tk.Button(self, text="collect", command = lambda: self.root.dmap.collect(pos))
        self.villagers.pack(side=tk.TOP)

        self.villagers = tk.Button(self, text="villagers", command = self.villagers_start)
        self.villagers.pack(side=tk.TOP)

        

        self.show()
    
    def error(self, msg):
        message = tk.Label(self, text= msg, bg="red")
        message.pack()
        self.show()
    
    def villagers_start(self):
        self.vil = Popup(self, self.size_x, self.size_y, self.x+self.size_x-50, self.y+self.size_y-50, 
                         self.size_x-100, self.size_y-100)
        village = self.village
        self.vil.villagers(village.persons_count, village.housed, village.homeless)
        self.vil.show()

    def villagers(self, nb_vil, housed, homeless):
        self.list = tk.Canvas(self, bg="white")
        y = 10
        for p in housed.values():
            text1 = "housed // name: " + p.name + " age: " + str(p.age) + " expectancy: " + str(p.expectancy)
            text2 = "mood: " + str(p.mood) + " wealth: " + str(p.wealth) + " fed: " + str(p.fed) + " food:" + str([p.food])
            self.list.create_text(100, y, text= text1, fill="black")
            self.list.create_text(100, y+25, text= text2, fill="black")
            y+=50
        for p in homeless.values():
            text1 = "homeless // name: " + p.name + " age: " + str(p.age) + " expectancy: " + str(p.expectancy)
            text2 = "mood: " + str(p.mood) + " wealth: " + str(p.wealth) + " fed: " + str(p.fed) + " food:" + str([p.food])
            self.list.create_text(100, y, text= text1, fill="black")
            self.list.create_text(100, y+25, text= text2, fill="black")
            y+=50

        self.scrollbar = tk.Scrollbar(self.list, command=self.list.yview)
        self.list.configure(yscrollcommand=self.scrollbar.set)
        self.list.pack(expand=True, fill = tk.BOTH, side=tk.RIGHT)
        self.scrollbar.pack(side=tk.RIGHT)
        tertext = str()

    def pause_menu(self):
        self.quit = tk.Button(self ,text= "Resume", height = 8, width = 50, command= self.root.destroy)
        self.quit.pack(side=tk.TOP)
        self.quit = tk.Button(self ,text= "Settings", height = 8, width = 50, command= self.root.destroy)
        self.quit.pack(side=tk.TOP)
        self.quit = tk.Button(self ,text= "Save", height = 8, width = 50, command= self.root.destroy)
        self.quit.pack(side=tk.TOP)
        self.quit = tk.Button(self ,text= "Save & Quit", height = 8, width = 50, command= self.root.destroy)
        self.quit.pack(side=tk.TOP)
        self.quit = tk.Button(self ,text= "Load", height = 8, width = 50, command= self.root.destroy)
        self.quit.pack(side=tk.TOP)
        self.quit = tk.Button(self ,text= "Main Menu", height = 8, width = 50, command= self.root.destroy)
        self.quit.pack(side=tk.TOP)
        self.quit = tk.Button(self ,text= "Quit", bg="red", height = 8, width = 50, command= self.root.destroy)
        self.quit.pack(side=tk.TOP)
    
    def help(self, comment):
        titre = tk.Label(self, text= comment)
        titre.pack(side=tk.TOP)

        self.villagers = tk.Button(self, text="next", command = self.root.next_help)
        self.villagers.pack(side=tk.TOP)
        self.show()

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








