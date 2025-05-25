from tkinter import *
from tkinter.ttk import Progressbar

window = Tk()
window.title("Progressbar Example")
window.geometry('400x250')

bar = Progressbar(window, length=200)
bar['value'] = 70
bar.grid(column=0, row=0)

window.mainloop()