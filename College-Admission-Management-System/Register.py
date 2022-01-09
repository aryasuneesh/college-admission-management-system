from tkinter import *
import tkinter.messagebox                               
import os                                                                
import random                                           
import time
import datetime
import sqlite3

def insert(id = 'NULL', username = ' ', password = ' ', confirm = ' '):
       con = sqlite3.connect('collegeadmn.db')
       cur = con.cursor()

       cur.execute('INSERT INTO register VALUES (NULL,?,?,?)',(username, password, confirm))

       con.commit()
       con.close()
       
def Add():
    if(len(Username.get())!= 0 and Password.get()==Confirm.get()):
        insert(username = Username.get(), password = Password.get(), confirm = Confirm.get())
        tkinter.messagebox.showinfo("Login", "Account Successfully Created")
        Exit()

    elif(Password.get()!=Confirm.get()):
        tkinter.messagebox.showerror("Login", "Error : Password Not Matching")
        Username.set("")
        Password.set("")
        Confirm.set("")
        text_Username.focus()
    else:
        tkinter.messagebox.showerror("Error", "Error! Please try again")
        Username.set("")
        Password.set("")
        Confirm.set("")
        text_Username.focus()

def Exit():
    Exit = tkinter.messagebox.askokcancel("Login System", "Confirm if you want to Exit")
    if Exit > 0:
        master.destroy()
        return 
        
master = Tk()


master.title("Student Registration")
master.geometry('1400x1200')
master.config(bg = 'orange')
Frame = Frame(master, bg = 'orange')
Frame.pack()


Username = StringVar()                             
Password = StringVar()
Confirm = StringVar()

Lbl_title = Label(Frame, text = 'Bengaluru Institute of Science and Technology', font = ('arial',40,'bold'), bg = 'orange', fg = 'Black')
Lbl_title.grid(row = 0, column = 0, columnspan =5, pady = 20)
Lbl_name = Label(Frame, text = 'Student Registration', font = ('arial',40,'bold'), bg = 'orange', fg = 'Black')
Lbl_name.grid(row = 1, column = 0, columnspan =5, pady = 20)

Reg_Frame_1 = LabelFrame(Frame, width = 1350, height = 600, relief = 'ridge', bg = 'orange', bd = 15, font = ('arial',20,'bold'))
Reg_Frame_1.grid(row = 3, column =0, columnspan =5)
Reg_Frame_2 = LabelFrame(Frame, width = 1000, height = 600, relief = 'ridge',bg = 'orange', bd = 15, font = ('arial',20,'bold'))
Reg_Frame_2.grid(row = 4, column = 0, columnspan =5)

#USERNAME AND PASSWORD
Label_Username = Label(Reg_Frame_1, text = 'Username', font = ('arial',20,'bold'), bg = 'orange', bd = 20)
Label_Username.grid(row = 0, column = 0)
text_Username = Entry(Reg_Frame_1, font = ('arial',20,'bold'), textvariable = Username)
text_Username.grid(row = 0, column = 1, padx = 50)                       

Label_Password = Label(Reg_Frame_1, text = 'Password', font = ('arial',20,'bold'), bg = 'orange', bd = 20)
Label_Password.grid(row = 1, column = 0)
text_Password = Entry(Reg_Frame_1, font = ('arial',20,'bold'), show = '*', textvariable = Password)
text_Password.grid(row = 1, column = 1)

Label_Confirm = Label(Reg_Frame_1, text = 'Confirm Password', font = ('arial',20,'bold'), bg = 'orange', bd = 20)
Label_Confirm.grid(row = 2, column = 0)
text_Confirm = Entry(Reg_Frame_1, font = ('arial',20,'bold'), show = '*', textvariable = Confirm)
text_Confirm.grid(row = 2, column = 1)


btnReg = Button(Reg_Frame_2, text = 'Register', width = 10, font = ('airia',15,'bold'), command = Add)
btnReg.grid(row = 3, column = 0, padx = 8, pady = 20)

btnExit = Button(Reg_Frame_2, text = 'Exit', width = 10, font = ('airia',15,'bold'), command = Exit)
btnExit.grid(row = 3, column = 1, padx = 8, pady = 20)



