from tkinter import *
from tkinter import filedialog
from os import path

window = Tk()
window.title("Filedialog Example")
window.geometry('400x250')

file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
print(file)

dir = filedialog.askdirectory()
print(dir)

file2 = filedialog.askopenfilename(initialdir= path.dirname(__file__))
print(file2)

window.mainloop()