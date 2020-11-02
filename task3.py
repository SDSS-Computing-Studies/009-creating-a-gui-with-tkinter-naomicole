#!python3

import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")

dogphoto = PhotoImage(file="dog.png")
labeld = tk.Label(window,image=dogphoto)
