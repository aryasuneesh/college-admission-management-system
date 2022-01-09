from tkinter import *
import tkinter.messagebox
import random
import sqlite3
import Clg_Details_BackEnd
from tkinter import ttk


global master

master = Tk()

master.title('College Details')
master.geometry('2150x850')
master.config(bg = 'orange')

name = StringVar()
cno = StringVar()
ano = StringVar()
address = StringVar()
mobno = StringVar()
email = StringVar()
det = StringVar()
      
def Display():
       listbox.delete(0, END)
       for row in Clg_Details_BackEnd.view():
            listbox.insert(END, row, str(' '))


def Exit():
       Exit = tkinter.messagebox.askyesno("Login System", "Confirm if you want to Exit")
       if Exit > 0:
              master.destroy()
              return


Main_Frame = LabelFrame(master, width = 2700, height = 500, font = ('arial',15,'bold'), bg = 'DarkOrange1',bd = 15)

Main_Frame.grid(row = 0, column = 0, columnspan = 4, padx = 60, pady = 20)


Frame_1 = LabelFrame(Main_Frame, width = 2250, height = 400, font = ('arial',15,'bold'), relief = 'ridge', bd = 10, bg = 'DarkOrange1', text = 'COLLEGE DETAILS')
Frame_1.grid(row = 1, column =1, columnspan =4, padx =60, pady = 60)

Frame_3 = LabelFrame(master, width = 2200, height = 100, font = ('arial',10,'bold'), bg = 'DarkOrange1', relief = 'ridge', bd = 13)
Frame_3.grid(row = 2, column = 0,columnspan =4, pady = 20)


btnDisplay = Button(Frame_3, text = 'DISPLAY', font = ('arial',13,'bold'), width = 8, command = Display)
btnDisplay.grid(row = 0, column = 1, padx = 10, pady = 10)

btnExit = Button(Frame_3, text = 'EXIT', font = ('arial',13,'bold'), width = 8, command = Exit)
btnExit.grid(row = 0, column = 2, padx = 10, pady = 10)


dat = Clg_Details_BackEnd.view()

name_label = Label(Frame_1, text ='Name: '+dat[0][1], font = ('arial',12,'bold'),  bg = 'DarkOrange1', wraplength=500)
name_label.grid(row = 0, column = 0, padx = 140, pady = 20)
cno_label = Label(Frame_1, text ='College No: '+dat[0][2], font = ('arial',12,'bold'),  bg = 'DarkOrange1', wraplength=500)
cno_label.grid(row = 1, column = 0, sticky = N, padx = 140, pady = 20)
ano_label=Label(Frame_1, text ='Affliation No: '+dat[0][3], font = ('arial',12,'bold'),  bg = 'DarkOrange1', wraplength=500)
ano_label.grid(row = 2, column = 0, sticky = N, padx = 140, pady = 20)
address_label =Label(Frame_1, text ='Address: '+dat[0][4], font = ('arial',12,'bold'),  bg = 'DarkOrange1', wraplength=500)
address_label.grid(row = 3, column = 0, sticky = N, padx = 140, pady = 20)
mobno_label =Label(Frame_1, text ='Mobile No: '+ str(dat[0][5]), font = ('arial',12,'bold'),  bg = 'DarkOrange1', wraplength=500)
mobno_label.grid(row = 4, column = 0, sticky = N, padx = 140, pady = 20)
emailID_label=Label(Frame_1, text ='Email ID: '+dat[0][6], font = ('arial',12,'bold'),  bg = 'DarkOrange1', wraplength=500)
emailID_label.grid(row = 5, column = 0, sticky = N, padx = 140, pady = 20)
det_label=Label(Frame_1, text ='Details: '+dat[0][7], font = ('arial',12,'bold'),  bg = 'DarkOrange1', wraplength=800)
det_label.grid(row = 6, column = 0, sticky = N, padx = 200, pady = 20)

master.mainloop()   


