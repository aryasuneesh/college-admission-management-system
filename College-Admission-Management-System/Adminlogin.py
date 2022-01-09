from tkinter import *
import tkinter.messagebox                               
import os                                                            
import random                                           
import time
import datetime



    
def Reset():
     user.set("")
     pwd.set("")
     text_Username.focus()



def Exit():
    Exit = tkinter.messagebox.askokcancel("Login System", "Confirm if you want to Exit")
    if Exit > 0:
        master.destroy()
        return

def adminmenu():
    fn = 'AdminMenu.py'
    os.system(fn)
    os.system('notepad'+fn)

def login():
    un = user.get()
    pw = pwd.get()

    if (un == str('clgadmin') and pw == str(12345)):
        adminmenu()
    else:
        tkinter.messagebox.askyesno("Login", "Error : Wrong Password")
        user.set("")
        pwd.set("")
        text_Username.focus()
                                         

master = Tk()

master.title("Admin Login")
master.geometry('1400x1200')
master.config(bg = 'orange')
frame = Frame(master, bg = 'orange')
frame.pack()

user = StringVar()
pwd = StringVar()

#================================================================================

Lbl_title = Label(frame, text = 'Bengaluru Institutes of Science and Technology', font = ('arial',40,'bold'), bg = 'orange', fg = 'Black')
Lbl_title.grid(row = 0, column = 0, columnspan =5, pady = 20)
Lbl_name = Label(frame, text = 'College Admission System - Admin', font = ('arial',40,'bold'), bg = 'orange', fg = 'Black')
Lbl_name.grid(row = 1, column = 0, columnspan =5, pady = 20)

Login_Frame_1 = LabelFrame(frame, width = 1350, height = 600, relief = 'ridge', bg = 'orange', bd = 15, font = ('arial',20,'bold'))
Login_Frame_1.grid(row = 3, column =0, columnspan =5)
Login_Frame_2 = LabelFrame(frame, width = 1000, height = 600, relief = 'ridge',bg = 'orange', bd = 15, font = ('arial',20,'bold'))
Login_Frame_2.grid(row = 4, column = 0, columnspan =5)


#LABEL AND ENTRIES
Label_Username = Label(Login_Frame_1, text = 'Admin Username', font = ('arial',20,'bold'), bg = 'orange', bd = 20)
Label_Username.grid(row = 0, column = 0)
text_Username = Entry(Login_Frame_1, font = ('arial',20,'bold'), textvariable = user)
text_Username.grid(row = 0, column = 1, padx = 50)                       

Label_Password = Label(Login_Frame_1, text = 'Password', font = ('arial',20,'bold'), bg = 'orange', bd = 20)
Label_Password.grid(row = 1, column = 0)
text_Password = Entry(Login_Frame_1, font = ('arial',20,'bold'), show = '*', textvariable = pwd)
text_Password.grid(row = 1, column = 1) 


#BUTTONS
btnLogin = Button(Login_Frame_2, text = 'Login', width = 10, font = ('airia',15,'bold'), command = login)
btnLogin.grid(row = 3, column = 0, padx = 8, pady = 20)

btnReset = Button(Login_Frame_2, text = 'Reset', width = 10, font = ('airia',15,'bold'), command = Reset)
btnReset.grid(row = 3, column = 1, padx = 8, pady = 20)

btnExit = Button(Login_Frame_2, text = 'Exit', width = 10, font = ('airia',15,'bold'), command = Exit)
btnExit.grid(row = 3, column = 2, padx = 8, pady = 20)


        
master.mainloop()




