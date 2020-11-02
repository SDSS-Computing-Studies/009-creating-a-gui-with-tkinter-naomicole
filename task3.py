#!python3

import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")

dogphoto = PhotoImage(file="dog.png")
labeld = tk.Label(window,image=dogphoto)
label1 = tk.Label(window,text="Pochacco!")
label2 = tk.Label(window, text="A cuddly little puppy! This is from the same\n creators who brought you Keropi and Kero Kero",bg="CadetBlue1")

labeld.grid(row = 1, column = 2, rowspan = 3)
label1.grid(row = 2, column = 3)
label2.grid(row = 4, column = 1, columnspan = 4)

window.mainloop()