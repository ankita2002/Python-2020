from tkinter import *
from sys import *
from PIL import Image, ImageTk
import pygame as py
import os
from random import randrange

py.init()

#Function runs the actual game. 
def runGame(startWindow):

#Close [startWindow] before advancing:
startWindow.destroy()
startWindow.quit()

master = Tk()
master.title('Lets Play!')

#Function carries on the remainder of the game.
def carryGame(button_id):

    result = StringVar()
    printResult = Label(master, textvariable = result, font='Bizon 32 bold', bg='PeachPuff2')
    printResult.place(x=150, y=300)

    #Computer's move:
    random_Num = randrange(1,4)

    if random_Num == 1:
       computer_Move = 'Rock'

    elif random_Num == 2:
        computer_Move = 'Paper'

    else:
        computer_Move = 'Scissors'

    if button_id == 1:
        player_Move = 'Rock'

    elif button_id == 2:
        player_Move = 'Paper'

    else:
        player_Move = 'Scissors'

#Rock button
rock_Button = Button(master, width=15, height=7, command=lambda:carryGame(1))
rock_photo=PhotoImage(file=r'C:\Users\Pamal\Desktop\Documents\Python Folder\Python Projects\Rock, Paper, Scissors\V 1.2\Images\rock.png')
rock_Button.config(image=rock_photo,width="120",height="120")
rock_Button.place(x=17, y=70)

#Paper button
paper_Button = Button(master, width=15, height=7, command=lambda:carryGame(2))
paper_photo=PhotoImage(file=r'C:\Users\Pamal\Desktop\Documents\Python Folder\Python Projects\Rock, Paper, Scissors\V 1.2\Images\paper.png')
paper_Button.config(image=paper_photo,width="120",height="120")
paper_Button.place(x=167, y=70)

#Scissors button
scissors_Button = Button(master, width=15, height=7, command=lambda:carryGame(3))
scissors_photo=PhotoImage(file=r'C:\Users\Pamal\Desktop\Documents\Python Folder\Python Projects\Rock, Paper, Scissors\V 1.2\Images\scissors.png')
scissors_Button.config(image=scissors_photo,width="120",height="120")
scissors_Button.place(x=317, y=70)

label_1 = Label(master, text='Please make your selection-', font='Bizon 20 bold', bg='PeachPuff2')
label_1.pack(side=TOP)

label_2 = Label(master, text='The computer picked:', font='Helvetica 22 bold', bg='PeachPuff2')
label_2.place(x=70, y=240)

#Locks window size
master.maxsize(450, 400)
master.minsize(450, 400)

#Sets window background to PeachPuff2
master.config(background='PeachPuff2')

master.mainloop()

def startScreen():

    #Plays music for the application
    def playMusic(fileName):
        py.mixer.music.load(fileName)
        py.mixer.music.play()

    #Start Window
    startWindow = Tk()
    startWindow.title('[Rock] [Paper] [Scissors]')

    #Imports image as title
    load = Image.open(r'C:\Users\Pamal\Desktop\Documents\Python Folder\Python Projects\Rock, Paper, Scissors\V 1.2\Images\title.png')
    render = ImageTk.PhotoImage(load)
    img = Label(startWindow, image=render, bd=0)
    img.image = render
    img.place(x=-100, y=-65)

    clickToPlay = Button(startWindow, text='Play!', width=8, font='Bizon 20 bold', bg='Black', fg='Yellow', relief=RIDGE, bd=0, command=lambda:runGame(startWindow))
    clickToPlay.place(x=75, y=125)

    #Credit
    authorName = Label(startWindow, text='Written by : Pamal Mangat', font='Times 6 bold', bg='Black', fg='Yellow')
    authorName.place(x=2, y=230)

    versionNum = Label(startWindow, text='[V 1.2]', font='Times 6 bold', bg='Black', fg='Red')
    versionNum.place(x=268, y=230)

    #Start Screen Music
    playMusic(r'C:\Users\Pamal\Desktop\Documents\Python Folder\Python Projects\Rock, Paper, Scissors\V 1.2\Audio\title_Song.mp3')

    #Locks window size
    startWindow.maxsize(300, 250)
    startWindow.minsize(300, 250)

    #Sets window background to black
    startWindow.config(background='Black')

    startWindow.mainloop()

startScreen()
