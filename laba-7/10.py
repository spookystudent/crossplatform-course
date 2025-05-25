from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Messagebox Yes/No Example")
window.geometry('400x250')

res = messagebox.askyesno('Заголовок', 'Текст')
print(res)

window.mainloop()