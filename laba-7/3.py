from tkinter import Button, Label, Tk

window = Tk()
window.title('Project')
window.geometry('400x250')

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

btn = Button(
    window,
    text="Click Me",
    command=lambda : lbl.configure(text="button was clicked")
)
btn.grid(column=1, row=0)

window.mainloop()