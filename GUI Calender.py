from tkinter import *
import calendar
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
    Exit = Button(gui, text = "EXIT",fg="Black",bg="Red", command= exit)

    cal.grid(row =1,column=1)
    year.grid(row=5,column=1)
    yearField.grid(row=6,column=1)
    Show.grid(row=8,column=1)
    Exit.grid(row=9,column=1)
    gui.mainloop()