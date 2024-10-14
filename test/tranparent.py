import tkinter as tk
from PIL import Image, ImageTk

COIN = "../img/money.png"
FOOD = "../img/food.png"


root = tk.Tk()

canv = tk.Canvas(root, width = 500, height = 500, bg='grey')
canv.pack()

im = Image.open(COIN)
img = ImageTk.PhotoImage(im)
canv.create_image(64, 64, image=img)

im2 = Image.open(FOOD)
img2 = ImageTk.PhotoImage(im2)
canv.create_image(164, 164, image=img2)

root.mainloop()