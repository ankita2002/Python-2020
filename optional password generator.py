from tkinter import*
import pyperclip 
import random
root=Tk()
root.geometry("400x400")
passstr=StringVar()
passlen=IntVar()
passlen.set(0)

def lower():
        al =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        password=""
        for x in range(passlen.get()):
            password=password+random.choice(al)
            passstr.set(password)

def upper():
        au =  ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        password=""
        for x in range(passlen.get()):
            password=password+random.choice(au)
            passstr.set(password)

def lowup():
        aul =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        password=""
        for x in range(passlen.get()):
            password=password+random.choice(aul)
            passstr.set(password)

def number():
        an =  ['1','2','3','4','5','6','7','8','9','0']
        password=""
        for x in range (passlen.get()):
            password=password+random.choice(an)
            passstr.set(password)

def charnum():
        acn =  ['1','2','3','4','5','6','7','8','9','0','!','~','@','#','$','%','^','&','*','(',')']
        password=""
        for x in range(passlen.get()):
            password=password+random.choice(acn)
            passstr.set(password)
 

def mix():
    listpass =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','~','@','#','$','%','^','&','*','(',')']
    password=""
    for x in range(passlen.get()):
        password=password + random.choice(listpass)
        passstr.set(password)

def copytoclipboard():
    randompassword = passstr.get()
    pyperclip.copy(randompassword)

Label(root, text = "PASSWORD GENERATOR APPLICATION", font="Helvetica 20 bold").pack()
Label(root, text = "ENTER PASSWORD LENGTH").pack(pady=3)
Entry(root,textvariable=passlen).pack(pady=3)
Label(root,text="OPTIONS:",font = "Helvetica 10 bold").pack()
Label(root,text="PRESS ANY BUTTON ACCORDING TO YOUR REQUIREMENT",font="calibri 10 bold").pack()
Button(root, text = "NUMBERS",command=number).pack(pady=7)
#Entry(root, textvariable=passstr).pack(pady=3)
Button(root, text = "GENERATE MIX PASSWORD",command=mix).pack(pady=7)
#Entry(root,textvariable=passlen).pack(pady=3)
Button(root,text="CHARACTER + NUMBERS",command=charnum).pack(pady=7)
#Entry(root, textvariable=passstr).pack(pady=3)
Button(root, text = "LOWERCASE ALPHABETS",command=lower).pack(pady=7)
#Entry(root, textvariable=passstr).pack(pady=3)
Button(root, text = "UPPERCASE ALPHABETS",command=upper).pack(pady=7)
#Entry(root, textvariable=passstr).pack(pady=3)
Button(root, text = "UPPERCASE + LOWERCASE ALPHABETS",command=lowup).pack(pady=7)
Entry(root, textvariable=passstr, font="Helvetica 10 bold").pack(pady=3)

Button(root, text="COPY TO CLIPBOARD",command=copytoclipboard).pack()
#Entry(root, textvariable=passstr).pack(pady=3)

root.mainloop()


