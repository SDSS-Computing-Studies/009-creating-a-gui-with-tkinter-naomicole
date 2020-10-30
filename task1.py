#!python3

import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("tk")

nF = Frame()

entry1 = tk.Entry(nF,text="entry one", width=15)
label1 = tk.Label(nF,text="x")
entry2 = tk.Entry(nF,text="entry two", width=15)
button1 = tk.Button(nF,text="=")
entry3 = tk.Entry(nF,text="entry three", width=25)

nF.pack()
entry1.pack(side=LEFT)
label1.pack(side=LEFT)
entry2.pack(side=LEFT)
button1.pack(side=LEFT)
entry3.pack(side=LEFT)

window.mainloop()