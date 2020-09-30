from tkinter import *

from random import choice



lis=["green","blue","red","black","white","yellow"]





root=Tk()

root.geometry("1040x1900")



c1=Canvas(root,height=1900,width=1040,background="grey")

c1.pack(fill="both")



def texts(row,column):

 text=color()

 fill=color()

 while text==fill:

  fill=color()

 c1.create_text(row,column,text=text,fill=fill,font="comicsanns 10")



def color():

 return str(choice(lis))



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



root.mainloop()
