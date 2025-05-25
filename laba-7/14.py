from tkinter import *
from tkinter import Menu

def clicked():
    pass

window = Tk()
window.title("Menu Example")
window.geometry('400x250')

menu = Menu(window)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Новый', command=clicked)
menu.add_cascade(label='Файл', menu=new_item)
window.config(menu=menu)

window.mainloop()