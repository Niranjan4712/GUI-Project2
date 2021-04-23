import tkinter
from tkinter import *

j=Tk()

j.geometry("300x300")
j.title('GUI basic button dimesion changes')


btnred = Button(j,text="Btton",fg="Red",bg="black")
btnred.place(x=20)
btnorg = Button(j,text="Orange",fg="Orange")
btnorg.pack(side=TOP)
btngreen=Button(j,text="Green",fg="Green")
btngreen.pack(side=BOTTOM)
btnyellow=Button(j,text="Yellow",fg="Yellow")
btnyellow.pack(side=LEFT)

j.mainloop()