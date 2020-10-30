#!python3

import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")
window.geometry("500x200")

button1 = tk.Button(window,text="Search by Name")
button2 = tk.Button(window,text="< Previous")
button3 = tk.Button(window,text="Save Entry")
button4 = tk.Button(window,text="Next >")
dogphoto = PhotoImage(file="dog.png")
labeld = tk.Label(window,image=dogphoto)
label1 = tk.Label(window,text="Client Database")
label2 = tk.Label(window,text="Name")
label3 = tk.Label(window,text="Type")
label4= tk.Label(window,text="Breed")
label5= tk.Label(window,text="Owner")
label6 = tk.Label(window,text="Birthdate")
entry1 = tk.Entry(window,text="entry1",width=20)
entry2 = tk.Entry(window,text="entry2",width=15)
entry3 = tk.Entry(window,text="entry3",width=15)
entry4 = tk.Entry(window,text="entry4",width=15)
entry5 = tk.Entry(window,text="entry5",width=15)
entry6 = tk.Entry(window,text="entry6",width=15)

labeld.place(x=0,y=0)
button1.place(x=275,y=0)
entry1.place(x=375,y=3)
label1.place(x=200,y=50)
label2.place(x=25,y=100)
label3.place(x=130,y=100)
label4.place(x=225,y=100)
label5.place(x=325,y=100)
label6.place(x=425,y=100)
entry4.place(x=275,y=100)
entry2.place(x=1,y=120)
entry3.place(x=100,y=120)
entry4.place(x=200,y=120)
entry5.place(x=300,y=120)
entry6.place(x=400,y=120)
button2.place(x=1,y=170)
button3.place(x=200,y=170)
button4.place(x=452,y=170)

window.mainloop()