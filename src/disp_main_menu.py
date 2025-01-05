import tkinter as tk
import disp_scene as ds
import game as gm
import disp_header as disp

class Main_Menu(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("1920x1080")
        self.im = tk.PhotoImage(disp.FRONT_PAGE)
        self.bg = tk.Label(self, image = self.im)
        self.bg.place(x=0, y=0, relwidth=1, relheight=1)

        self.start_button = tk.Button(self, text ="start", command=self.launch) 
        self.start_button.pack()
        self.bg.pack()
        self.mainloop()

    def launch(self):
        self.game = gm.Game("savefile")
        self.ds  = ds.Scene(self, self.game)
        self.ds.mainloop()


if __name__ == "__main__":
    root = Main_Menu()