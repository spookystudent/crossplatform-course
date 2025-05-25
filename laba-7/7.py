from tkinter import *

def clicked():
    lbl.configure(text=selected.get())

window = Tk()
window.title("Radiobutton Example")
window.geometry('400x250')

selected = IntVar()
selected.set(1)

rad1 = Radiobutton(window, text='Первый', value=1, variable=selected)
rad2 = Radiobutton(window, text='Второй', value=2, variable=selected)
rad3 = Radiobutton(window, text='Третий', value=3, variable=selected, command=clicked)

rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)

lbl = Label(window)
lbl.grid(column=0, row=1)

window.mainloop()