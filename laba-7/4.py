from tkinter import Button, Entry, Label, Tk

window = Tk()
window.title('Project')
window.geometry('400x250')

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

txt = Entry(window, text="Enter your text here:")
txt.grid(column=1, row=0)

btn = Button(window, text="Click Me", command=lambda : lbl.configure(text=f"Hello, {txt.get()}"))
btn.grid(column=2, row=0)

window.mainloop()