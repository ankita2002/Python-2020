from getpass import getpass
from hashlib import sha1
import pyperclip
import tkinter as tk 

def check():
    if password != repeat:
        see_label["text"]="PASSWORD DID NOT MATCH"

    
    a = sha1(password.encode('utf-8'))
    see_label["text"]= "SHA-1: " +a.hexdigest()


window=tk.Tk()
window.geometry("500x260") #width x height
window.grid_columnconfigure((0,1), weight=1)
window.title("SHA-1")
passw = tk.Label(
    text="Enter Password: ",
    width=30,
    font=('Helvetica', 12, 'bold')
)
password=tk.Entry( width =20)

repass=tk.Label(
    text="Repeat Password: ", 
    width=30,
    font=('Helvetica',12, 'bold')
)
repeat=tk.Entry(width=20)

see=tk.Label(
    height=3,
    width=20,
    bg='white',
    fg='black',
        font=('Times New Roman', 12, 'italic')

)

Result=tk.Button(
    text='RESULT',
    height=1,
    width=20,
    bg='red',
    fg='black',
    command = check ,
    font=('Times New Roman', 12, 'italic')
)
texts=tk.Label(
    text="PS-Password is not visible ",
    height=1,
    width=20,
    font=('Helvetica', 12, 'bold')
)
about=tk.Label(
    text='''
    This is a created by Ankita Upadhyay. 
    Suggestions are welcome.Contact-9920315721
    ''',
    fg="grey",
    height=2,)

passw.grid(row=1,columnspan=1)
password.grid(row=1,columnspan=2)
repass.grid(row=3,columnspan=1)
repeat.grid(row=3,columnspan=2)
texts.grid(row=4,columnspan=1)
Result.grid(row=6,columnspan=2)
see.grid(row= 8,columnspan=2)
about.grid(row=10,columnspan=2)
window.mainloop()












