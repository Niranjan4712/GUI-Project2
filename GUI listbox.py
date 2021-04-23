import tkinter
from tkinter import *
j=Tk()
j.title('GUI listbox widgets ')
j.geometry('500x600')
m=Listbox()
m.insert(1,'Name')
m.insert(2,'Contact')
m.insert(3,'Address')
m.insert(4,'City')
m.insert(5,'Profile')
m.pack()

mainloop()
