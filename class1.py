from tkinter import *


#Everything is a widget just like flutter

#initialize the window and the app
root = Tk()
#title of the window
root.title('First class')

myLabel = Label(root, text='Hello Tkinter',height=100, width=1000)

#pack()--> show on your root or whatever windows u had indicated
myLabel.pack()

#size of the window
root.geometry('6000x700')


#event loops
root.mainloop()
