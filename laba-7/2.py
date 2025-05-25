from tkinter import Label, Tk

window = Tk()
window.title('Project')
window.geometry('400x250')

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

window.mainloop()