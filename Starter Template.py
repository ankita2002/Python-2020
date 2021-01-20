

from tkinter import *  #make sure you install tkinter through Cmd - "pip install tkinter" 

class Tkinter_Template(object):       #to create frame for tkinter template 
    def __init__(self,master):
        frame = Frame(master)   
        frame.grid()                  #making window contents into grid
        label = Label(master,text="WELCOME TO CODE OWL \n follow us for more",font=(25),bg="Black",fg="Orange")
        label.grid(padx=50,pady=30)   #label section is all about content you want inside template  
                                      #inserting the label into the window

if __name__=='__main__':     
    root=Tk()                            #making root as handle for window
    root.title("Template using Tkinter") #giving title to window
    root.geometry("400x200")             #size of window
    Tkinter_Template(root)               #calling function to define and add Elements
    root.mainloop()                      #execute
