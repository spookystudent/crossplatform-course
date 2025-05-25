from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Messagebox Example")
window.geometry('400x250')

messagebox.showinfo('Заголовок', 'Текст')

window.mainloop()