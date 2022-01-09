from tkinter import *
import tkinter.messagebox                               
import os                                                                
import random                                           
import time
import datetime
import login_db

def Login():
    u = Username.get()
    p = Password.get()
    cred = login_db.view()
    len_cred = len(cred)
    for i in range(0, len_cred):
        if u == cred[i][1]:
            if p == cred[i][2] and p == cred[i][3]:
                __menu__()
            elif p!=cred[i][2]:
                tkinter.messagebox.showerror("Login", "Error : Password Not Matching")
                Username.set("")
                Password.set("")
                text_Username.focus()
                break
        else:
            tkinter.messagebox.showerror("Error", "Error! Please try again")
            Username.set("")
            Password.set("")
            text_Username.focus()
            break
    
def Reset():
     Username.set("")
     Password.set("")
     text_Username.focus()



def Exit():
    Exit = tkinter.messagebox.askokcancel("Login System", "Confirm if you want to Exit")
    if Exit > 0:
        master.destroy()
        return

def __menu__():
    filename = 'Menu.py'
    os.system(filename)
    os.system('notepad'+filename)
    
def __Adminlogin__():
    filename = 'Adminlogin.py'
    os.system(filename)
    os.system('notepad'+filename)
    
def __Register__():
    filename = 'Register.py'
    exec(open(filename).read())    


master = Tk()


master.title("Student Login")
master.geometry('1400x1200')
master.config(bg = 'orange')
Frame = Frame(master, bg = 'orange')
Frame.pack()


Username = StringVar()                             
Password = StringVar()

Lbl_title = Label(Frame, text = 'Bengaluru Institute of Science and Technology', font = ('arial',40,'bold'), bg = 'orange', fg = 'Black')
Lbl_title.grid(row = 0, column = 0, columnspan =5, pady = 20)
Lbl_name = Label(Frame, text = 'College Admission System', font = ('arial',40,'bold'), bg = 'orange', fg = 'Black')
Lbl_name.grid(row = 1, column = 0, columnspan =5, pady = 20)

Login_Frame_1 = LabelFrame(Frame, width = 1350, height = 600, relief = 'ridge', bg = 'orange', bd = 15, font = ('arial',20,'bold'))
Login_Frame_1.grid(row = 3, column =0, columnspan =5)
Login_Frame_2 = LabelFrame(Frame, width = 1000, height = 600, relief = 'ridge',bg = 'orange', bd = 15, font = ('arial',20,'bold'))
Login_Frame_2.grid(row = 4, column = 0, columnspan =5)


Label_Username = Label(Login_Frame_1, text = 'Username', font = ('arial',20,'bold'), bg = 'orange', bd = 20)
Label_Username.grid(row = 0, column = 0)
text_Username = Entry(Login_Frame_1, font = ('arial',20,'bold'), textvariable = Username)
text_Username.grid(row = 0, column = 1, padx = 50)                       

Label_Password = Label(Login_Frame_1, text = 'Password', font = ('arial',20,'bold'), bg = 'orange', bd = 20)
Label_Password.grid(row = 1, column = 0)
text_Password = Entry(Login_Frame_1, font = ('arial',20,'bold'), show = '*', textvariable = Password)
text_Password.grid(row = 1, column = 1) 


btnLogin = Button(Login_Frame_2, text = 'Login', width = 10, font = ('airia',15,'bold'), command = Login)
btnLogin.grid(row = 3, column = 0, padx = 8, pady = 20)

btnReset = Button(Login_Frame_2, text = 'Reset', width = 10, font = ('airia',15,'bold'), command = Reset)
btnReset.grid(row = 3, column = 1, padx = 8, pady = 20)

btnExit = Button(Login_Frame_2, text = 'Exit', width = 10, font = ('airia',15,'bold'), command = Exit)
btnExit.grid(row = 3, column = 2, padx = 8, pady = 20)

btnAdmLogin = Button(Login_Frame_2, text = 'Admin Login', width = 10, font = ('airia',15,'bold'), command = __Adminlogin__)
btnAdmLogin.grid(row = 4, column = 1, padx = 8, pady = 20)

btnRgstr= Button(Login_Frame_2, text = 'Register', width = 10, font = ('airia',15,'bold'), command = __Register__)
btnRgstr.grid(row = 4, column = 2, padx = 8, pady = 20)

master.mainloop()
