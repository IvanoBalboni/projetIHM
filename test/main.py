import tkinter as tk
import random as rand

class Example(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.canvas = tk.Canvas(self, background="black")
        #self.xsb = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        #self.ysb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        #self.canvas.configure(yscrollcommand=self.ysb.set, xscrollcommand=self.xsb.set)
        self.canvas.configure(scrollregion=(0,0,4000,4000))

        self.canvas.pack(expand=True, fill = tk.BOTH)

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


if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
