
try:
    import tkinter as tk
    from tkinter import ttk
except:
    import tkinter as tk
    import ttk

#the try and except block in python is used to catch and handle exceptions
#the except statement the programs response to any exception that occurs while preceding try clause
#we have imported tkinter as it is the standart GUI library

from tkcalendar import Calendar, DateEntry
from tkinter import *
import calendar

def check():
    top = tk.Toplevel(gui)
    ttk.Label(top, text= "Choose Date").pack(padx=10,pady=10)
    cal = DateEntry(top, width=12, background = "light pink", foreground="Black", borderwidth=2)
    cal.pack(padx=10,pady=10)
 #   top=tk.Tk()
    s=ttk.Style(root)
    s.theme_use('clam')
    top.mainloop()

def showCal():
    root = Tk()
    root.config(background = "blue")
    root.title("GUI CALENDAR")
    root.geometry("550x600")
    fetchYear =  int(yearField.get())
    calContent = calendar.calendar(fetchYear)
    calYear = Label(root,text= calContent, font ="Consolas 15 bold")
    calYear.grid(row = 5, column = 1, padx = 20)
    root.mainloop()

if __name__ == "__main__":
    gui = Tk()
    gui.config(background = "light pink")
    gui.title("CALENDAR")
    gui.geometry("250x200")
    cal = Label(gui,text="CALENDAR", bg = "white", font = ("times" , 28, 'bold'))
    year = Label(gui, text= "ENTER YEAR",bg="light green")
    yearField = Entry(gui)
    Show = Button(gui,text="SHOW CALENDAR", fg="Black" , bg="Yellow", command = showCal)
    Date= Button(gui,text ="CHECK DATE", fg="Black", bg="Yellow", command = check)
    Exit = Button(gui, text = "EXIT",fg="Black",bg="Red", command= exit)

    cal.grid(row =  1,column=1)
    year.grid(row=5,column=1)
    yearField.grid(row=6,column=1)
    Show.grid(row=8,column=1)
    Date.grid(row=10 ,column=1)
    Exit.grid(row=12,column=1)
    gui.mainloop()

