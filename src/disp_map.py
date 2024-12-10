import tkinter as tk
import random as rand
from PIL import Image, ImageTk
import os

COIN = "../img/money.png"
FOOD = "../img/food.png"
WOOD = "../img/wood.png"
CANCEL = "../img/cancel.png"

class Map(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.menucanvas = tk.Canvas(self, background="grey")

        self.root = root

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        print(self.screen_height)
        print(self.screen_width)
        print("hey")
        #'''
        self.configure(height = self.screen_height,
             width = self.screen_width)
        #self.root.resizable(height = None, width = None)'''

        im = Image.open(COIN)
        self.coin = ImageTk.PhotoImage(im)

        im = Image.open(FOOD)
        self.food = ImageTk.PhotoImage(im)

        im = Image.open(WOOD)
        self.wood = ImageTk.PhotoImage(im)

        im = Image.open(CANCEL)
        self.cancel = ImageTk.PhotoImage(im)

        self.money_button = tk.Button(self, text = "money", image=self.coin,
            height = 30, width = 150, compound="left", command = self.coin_popup)
        self.food_button = tk.Button(self, text = "food", image=self.food,
            height = 30, width = 150, compound="left", command = self.food_popup)
        self.wood_button = tk.Button(self, text = "wood", image=self.wood,
             height = 30, width = 150, compound="left", command = self.wood_popup)
        
        self.exit_button = tk.Button(self, image=self.cancel,
            height = 30, width = 30, command = self.root.destroy)


        self.canvas = tk.Canvas(self, background="black")
        #self.xsb = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        #self.ysb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        #self.canvas.configure(yscrollcommand=self.ysb.set, xscrollcommand=self.xsb.set)
        self.canvas.configure(scrollregion=(0,0,4000,4000))

        self.canvas.pack(expand=True, fill = tk.BOTH, side = tk.BOTTOM)

        self.money_button.pack(side=tk.LEFT)
        self.food_button.pack(side=tk.LEFT)
        self.wood_button.pack(side=tk.LEFT)

        self.exit_button.pack(side=tk.RIGHT)

        self.coin_popup_init()
        self.food_popup_init()
        self.wood_popup_init()

        #self.root.overrideredirect(True)

        print(self.canvas.cget("width"))
        print(self.canvas.cget("height"))

        mat = [ [rand.randint(0,3) for i in range(100)] for j in range(40) ]

        x, y = 0, 0
        size = 100
        texture = ['green', 'blue', 'grey', 'purple']

        for line in mat:
            for tile in line:
                self.canvas.create_rectangle(x, y, x+size, y+size, fill=texture[tile])
                y+=100
            x+=100
            y = 0

        # This is what enables scrolling with the mouse:
        self.canvas.bind("<ButtonPress-1>", self.scroll_start)
        self.canvas.bind("<B1-Motion>", self.scroll_move)

    def scroll_start(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def scroll_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)
    
    def coin_popup_init(self):
        self.coin_switch = False
        self.coin_menu = tk.Toplevel(self)
        self.coin_menu.geometry("170x200+5+110")
        self.coin_menu.overrideredirect(True)#retire bordures
        #self.wait_visibility(self)
        self.coin_menu.wm_attributes("-alpha", 0.3)#canal alpha (transparence)
        self.coin_menu.withdraw()
    
    def coin_popup(self):
        self.coin_switch = not self.coin_switch
        if(self.coin_switch):
            self.coin_menu.deiconify()
        else:
            self.coin_menu.withdraw()

    def food_popup_init(self):
        self.food_switch = False
        self.food_menu = tk.Toplevel(self)
        self.food_menu.geometry("170x200+182+110")
        self.food_menu.overrideredirect(True)#retire bordures
        self.food_menu.withdraw()
    
    def food_popup(self):
        self.food_switch = not self.food_switch
        if(self.food_switch):
            self.food_menu.deiconify()
        else:
            self.food_menu.withdraw()

    def wood_popup_init(self):
        self.wood_switch = False
        self.wood_menu = tk.Toplevel(self)
        self.wood_menu.geometry("170x200+359+110")
        self.wood_menu.overrideredirect(True)#retire bordures
        self.wood_menu.withdraw()
    
    def wood_popup(self):
        self.wood_switch = not self.wood_switch
        if(self.wood_switch):
            self.wood_menu.deiconify()
        else:
            self.wood_menu.withdraw()

    

if __name__ == "__main__":
    root = tk.Tk()
    Map(root).pack(fill="both", expand=True)
    root.mainloop()