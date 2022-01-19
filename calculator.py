import math
import re
from readline import insert_text
from tkinter import *
from webbrowser import get


def clicked(character, e:Tk):
 
    
    if character=='clear':
        e.delete(0,END)
        return    

    current= e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(character))
    

def operations(typee):
    global math
    math = typee
    print(typee)
    global first
    first = int(e.get()) 
    e.delete(0,END)
    



def equal():
    second_number = int(e.get())
    
    print(math)
    
    if math == 1:
        aux = first+second_number
        e.delete(0,END)
        e.insert(0,aux)
        
    elif math == 2:
        aux = first-second_number
        e.delete(0,END)
        e.insert(0,aux)
    
    elif math == 3:
        aux = first/second_number
        e.delete(0,END)
        e.insert(0,aux)
    
    elif math == 4:
        aux = first*second_number
        e.delete(0,END)
        e.insert(0,aux)
    
    elif math == 5:
        aux = first**second_number
        e.delete(0,END)
        e.insert(0,aux)


def put_buttons(e):
    button0=Button(root, text='0', padx=40, pady=20,command=lambda: clicked(0,e))
    button1=Button(root, text='1', padx=40, pady=20,command=lambda: clicked(1,e))
    button2=Button(root, text='2', padx=40, pady=20,command=lambda: clicked(2,e))
    button3=Button(root, text='3', padx=40, pady=20,command=lambda: clicked(3,e))
    button4=Button(root, text='4', padx=40, pady=20,command=lambda: clicked(4,e))
    button5=Button(root, text='5', padx=40, pady=20,command=lambda: clicked(5,e))
    button6=Button(root, text='6', padx=40, pady=20,command=lambda: clicked(6,e))
    button7=Button(root, text='7', padx=40, pady=20,command=lambda: clicked(7,e))
    button8=Button(root, text='8', padx=40, pady=20,command=lambda: clicked(8,e))
    button9=Button(root, text='9', padx=40, pady=20,command= lambda: clicked(9,e))
    buttonadd=Button(root, text='+', padx=40, pady=20,command=lambda: operations(1))
    buttonasub=Button(root, text='-', padx=40, pady=20,command= lambda: operations(2))
    buttonadiv=Button(root, text='÷', padx=40, pady=20,command=lambda: operations(3))
    buttonamult=Button(root, text='x', padx=40, pady=20,command=lambda: operations(4) )
    buttonpower = Button(root, text='^', padx=40, pady=20,command= lambda: operations(5))
    buttonequal=Button(root, text='=', padx=40, pady=20,command=equal)
    button_clear=Button(root,text='Clear', padx=79, pady=20,command=lambda: clicked('clear',e))
    
    #PUT THE BUTTONS ON THE SCREEN
        
    button0.grid(row=4,column=0)

    button1.grid(row=3,column=0)
    button2.grid(row=3,column=1)
    button3.grid(row=3,column=2)

    button4.grid(row=2,column=0)
    button5.grid(row=2,column=1)
    button6.grid(row=2,column=2)

    button7.grid(row=1,column=0)
    button8.grid(row=1,column=1)
    button9.grid(row=1,column=2)

    buttonadd.grid(row=4,column=1)
    buttonasub.grid(row=5,column=0)
    buttonamult.grid(row=5,column=1)
    buttonadiv.grid(row=5,column=2)
    buttonequal.grid(row=4,column=2)
    buttonpower.grid(row=6,column=0)
    button_clear.grid(row=6,column=1,columnspan=2)

    








if __name__ =="__main__":    
    
    
    
   #calling methods to open a window
    root  = Tk()
    #Defining screen resolutions
    root.geometry('300x450')
    root.title('Simple Calculator')
    #settig to not be resizable 
    root.resizable(False,False)

    #input box
    e = Entry(root, width=25, borderwidth=15)
    #put input box  in the screen
    e.grid(row=0, column=0, columnspan=3,padx=10, pady=10)

    put_buttons(e)
    
    root.mainloop()