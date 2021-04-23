import tkinter
from tkinter import *
j=Tk()
j.title('canvas widgets')
j.geometry('250x333')
canvas=Canvas(j,bg="red",height='300',width='200')
canvas2=Canvas(j,bg="blue",height='300',width='200')
canvas.pack()
canvas2.pack()
j.mainloop()
