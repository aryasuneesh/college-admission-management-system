from tkinter import *
import tkinter.messagebox
import random
import sqlite3
import Student_CutoffDisplay_Backend
from tkinter import ttk


global master

master = Tk()

master.title('Cutoff Details')
master.geometry('1130x800')
master.config(bg = 'orange')

intro = StringVar()
det = StringVar()
cutoff1 = StringVar()
cutoff2 = StringVar()
cutoff3 = StringVar()
cutoff4 = StringVar()
cutoff5 = StringVar()
cutoff6 = StringVar()
cutoff7 = StringVar()

Main_Frame = LabelFrame(master, width = 1000, height = 400, font = ('arial',14,'bold'), bg = 'DarkOrange1',bd = 12, text = 'CUTOFF DETAILS')

Main_Frame.grid(row = 0, column = 0, columnspan = 4, padx = 60, pady = 20)


dat = Student_CutoffDisplay_Backend.view()

intro_label = Label(Main_Frame, text ='Cutoff for 2020: ', font = ('arial',14,'bold', 'underline'),  bg = 'DarkOrange1', wraplength=500)
intro_label.grid(row = 0, column = 0, padx = 200, pady = 20)
det_label = Label(Main_Frame, text ='Showing Cut off values for JEE MAIN exam only. No reservations available', font = ('arial',14,'bold'),  bg = 'DarkOrange1', wraplength=500)
det_label.grid(row = 1, column = 0, sticky = N, padx = 200, pady = 20)
cutoff1_label=Label(Main_Frame, text ='Integrated B.Tech. + M.Tech. in Computer Science and Engineering:'+dat[0][1], font = ('arial',12,'bold'),  bg = 'DarkOrange1', wraplength=500)
cutoff1_label.grid(row = 2, column = 0, sticky = N, padx = 200, pady = 20)
cutoff2_label =Label(Main_Frame, text ='Integrated B.Tech. + M.Tech. in Electronics and Communication Engineering: '+dat[0][2], font = ('arial',12,'bold'),  bg = 'DarkOrange1', wraplength=500)
cutoff2_label.grid(row = 3, column = 0, sticky = N, padx = 200, pady = 20)
cutoff3_label =Label(Main_Frame, text ='B.Tech. in Computer Science and Engineering: '+dat[0][3], font = ('arial',12,'bold'),  bg = 'DarkOrange1', wraplength=500)
cutoff3_label.grid(row = 4, column = 0, sticky = N, padx = 200, pady = 20)
cutoff4_label=Label(Main_Frame, text ='B.Tech. in Electronics and Communication Engineering: '+dat[0][4], font = ('arial',12,'bold'),  bg = 'DarkOrange1', wraplength=500)
cutoff4_label.grid(row = 5, column = 0, sticky = N, padx = 200, pady = 20)
cutoff5_label=Label(Main_Frame, text ='B.Tech. in Aerospace Engineering: '+dat[0][5], font = ('arial',12,'bold'),  bg = 'DarkOrange1', wraplength=800)
cutoff5_label.grid(row = 6, column = 0, sticky = N, padx = 200, pady = 20)
cutoff6_label=Label(Main_Frame, text ='B.Tech. in Mechanical Engineering: '+dat[0][6], font = ('arial',12,'bold'),  bg = 'DarkOrange1', wraplength=800)
cutoff6_label.grid(row = 7, column = 0, sticky = N, padx = 200, pady = 20)
cutoff7_label=Label(Main_Frame, text ='For further details, email us at info@bit.ac.in', font = ('arial',14,'bold', 'underline'),  bg = 'DarkOrange1', wraplength=800)
cutoff7_label.grid(row = 8, column = 0, sticky = N, padx = 200, pady = 20)

master.mainloop()   


