import tkinter as tk
from PIL import Image, ImageTk

import disp_header as disp
import disp_map    as dmap
import disp_popup_factory as dp
import disp_popup_factory as pop
import game as gm

class Scene(tk.Tk):
    def __init__(self, game: gm.Game):
        tk.Tk.__init__(self)
        self.game = game

        self.attributes("-fullscreen", True)

        self.top_menu = tk.Frame(self)
        self.bot_menu = tk.Frame(self)

        im = Image.open(disp.COIN)
        self.coin = ImageTk.PhotoImage(im)
        im = Image.open(disp.CANCEL)
        self.cancel = ImageTk.PhotoImage(im)
        im = Image.open(disp.FOOD)
        self.food = ImageTk.PhotoImage(im)
        im = Image.open(disp.WOOD)
        self.wood = ImageTk.PhotoImage(im)
        im = Image.open(disp.MENU)
        self.menu = ImageTk.PhotoImage(im)
        im = Image.open(disp.END_TURN)
        self.end_turn = ImageTk.PhotoImage(im)

        self.exit_button = tk.Button(self.top_menu, image=self.cancel,
            height = 50, width = 50, command = self.destroy)
        
        self.menu_popup = pop.Popup(self, self.winfo_screenwidth(), self.winfo_screenheight(),
                                1920//3, 75,
                                2*(1920//3), self.winfo_screenheight()-150)
        
        self.menu_button = tk.Button(self.top_menu, image=self.menu,
            height = 50, width = 50, command = self.menu_popup.show)
        
        
        self.money_str= "money: " + str(self.game.pf.players[self.game.main_player].ressources[0])
        self.food_str = "food: " + str(self.game.pf.players[self.game.main_player].ressources[1])
        self.wood_str = "wood: " + str(self.game.pf.players[self.game.main_player].ressources[2])
        self.money_button = tk.Button(self.top_menu, text = self.money_str, image=self.coin,
            height = 50, width = 150, compound="left")
        self.food_button = tk.Button(self.top_menu, text = self.food_str, image=self.food,
            height = 50, width = 150, compound="left")
        self.wood_button = tk.Button(self.top_menu, text = self.wood_str, image=self.wood,
             height = 50, width = 150, compound="left")
        
        self.end_turn_button = tk.Button(self.bot_menu, image=self.end_turn,
            height = 50, width = 50, command = self.destroy)
        #self.screen_width = self.self.winfo_screenwidth()
        #self.screen_height = self.self.winfo_screenheight()
        #self.configure(height = self.screen_height, width = self.screen_width)

        self.game: gm.Game = game

        self.dmap: dmap.DMap = dmap.DMap(self, self.game.map, self.game.pf)

        
        self.top_menu.pack(side=tk.TOP, fill=None)
        #self.map_frame.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self.dmap.pack(expand=True, fill=tk.BOTH)
        self.bot_menu.pack(side=tk.BOTTOM,fill=None)

        self.end_turn_button.pack(side=tk.BOTTOM)

        self.money_button.pack(side=tk.LEFT)
        self.food_button.pack(side=tk.LEFT)
        self.wood_button.pack(side=tk.LEFT)
        self.exit_button.pack(side=tk.RIGHT)
        self.menu_button.pack(side=tk.RIGHT)

        print(self.winfo_screenwidth(), self.winfo_screenheight())

        self.help = None
        self.help_nb = 0
        self.help_list =["to move around the map, maintain your left click.",
                         "to see information on a Tile, right click on it.",
                         "the territories are inside a surlined color.",
                         "you can access the menu by clicking on the square at the top.",
                         "you can build a new village on a tile of your territory."]
        self.next_help()


        self.menu_popup.pause_menu()

        self.dmap.bind("<ButtonRelease-3>", self.dmap.tileMenu)
    
    def update_ressources(self):
        self.money_str= "money: " + str(self.game.pf.players[self.game.main_player].ressources[0])
        self.food_str = "food: " + str(self.game.pf.players[self.game.main_player].ressources[1])
        self.wood_str = "wood: " + str(self.game.pf.players[self.game.main_player].ressources[2])
        self.money_button.config(text = self.money_str)
        self.food_button.config(text = self.food_str)
        self.wood_button.config(text = self.wood_str)
    
    def next_help(self):
        if self.help is not None:
            self.help.destroy()
        self.help = self.help = pop.Popup(self, self.winfo_screenwidth(), self.winfo_screenheight(), 500, 500, 700, 400)
        self.help.help(self.help_list[self.help_nb])
        self.help_nb = (self.help_nb+1) % 5


if __name__ == "__main__":
    g = gm.Game("save")
    s = Scene(g)
    s.mainloop()