##imports##
from tkinter import *

from random import choice


lis=["green", "blue", "red", "black", "white", "yellow", "orange", "grey", "brown"]


root=Tk()

root.geometry("1040x1900")

def changebg():
 c1.config(background=choice(lis))

c1=Canvas(root,height=1900,width=1040,background="grey")

c1.pack(fill="both")



def texts(row,column):

 text=color()

 fill=color()

 while text==fill:

  fill=color()

 c1.create_text(row,column,text=text,fill=fill,font="comicsanns 10")

b1=Button(root,text="exit", command=root.destroy)
b1.pack()

def color():
 lis1=str(choice(lis))
 return lis1

height=100

def make(): 
 
 texts(100,height)

 texts(300,height)

 texts(500,height)

 texts(700,height)

 texts(900,height)


while height<1900: 

 make()
 
 height+=200 
changebg()
root.mainloop()
