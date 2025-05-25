from tkinter import *
from tkinter.ttk import Spinbox

window = Tk()
window.title("Spinbox Example")
window.geometry('400x250')

spin = Spinbox(window, from_=0, to=100, width=5)
spin.grid(column=0, row=0)

var = IntVar()
var.set(36)
spin2 = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
spin2.grid(column=1, row=0)

window.mainloop()