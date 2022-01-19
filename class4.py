#  INPUT DATA 
# Entry data

from distutils import command
from sqlite3 import Row
from struct import pack
from tkinter import *
from turtle import fd


#Everything is a widget just like flutter

#initialize the window and the app

root = Tk()


e = Entry(root, width= 50,bg='white', fg='black', borderwidth=12)
e.insert(0,'Enter your name')
e.pack()

#title of the window
root.title('First class')
x=0

def my_click():
    myLabel =Label(root, text=e.get())
    myLabel.pack()
    my_button.configure(state=DISABLED)
    
    
    
#bg means background color and fg foreground color    
my_button = Button(text='enter your name', padx=50, pady=20, command=my_click, fg='blue')
my_button.pack() 

root.mainloop()
