#  POSITIONING WITH TKINTER'S

# GRID SYSTEM
from sqlite3 import Row
from tkinter import *


#Everything is a widget just like flutter

#initialize the window and the app
root = Tk()
#title of the window
root.title('First class')



myLabel1 = Label(root, text='Hello Tkinter')
myLabel2 = Label(root, text='MY NAME IS PEDRO')


# It work with position in columns and rows and replace the pack() method

#they are relative to each other the number of colum or rows doesn't matter 
myLabel1.grid(row=3, column=2)
myLabel2.grid(row=0, column=9)


#size of the window
root.geometry('6000x700')


#event loops
root.mainloop()
