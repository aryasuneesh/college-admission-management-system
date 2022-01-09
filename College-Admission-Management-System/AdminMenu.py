from tkinter import *
import random
import os

def __collegedetails__():
       filename = 'Clg_Details_FrontEnd.py'
       os.system(filename)
       os.system('notepad'+filename)

def __studdetails__():
       filename = 'Std_reg_FrontEnd.py'
       os.system(filename)
       os.system('notepad'+filename)

def __cutoffdetails__():
       filename = 'Student_CutoffDisplayEdit_Frontend.py'
       os.system(filename)
       os.system('notepad'+filename)

       
       
def menu():
       root = Tk()
       root.title('Menu')
       root.geometry('1150x550')
       root.config(bg = 'orange')

       title_Frame = LabelFrame(root, font = ('arial',50,'bold'), width = 1000, height = 100, bg = 'orange', relief = 'raise', bd = 13)
       title_Frame.grid(row = 0, column = 0,  pady = 50)

       title_Label = Label(title_Frame, text = 'ADMIN MENU', font = ('arial',30,'bold'), bg = 'orange')
       title_Label.grid(row = 0, column = 0, padx = 150)


       #FRAMES
       Frame_1 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'orange', relief = 'ridge', bd = 10)
       Frame_1.grid(row = 1, column = 0, padx = 280)
       Frame_2 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'orange', relief = 'ridge', bd = 10)
       Frame_2.grid(row = 2, column = 0, padx = 130, pady = 7)
       Frame_3 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'orange', relief = 'ridge', bd = 10)
       Frame_3.grid(row = 3, column = 0, pady = 7)




       #LABELS
       Label_1 = Label(Frame_1, text = 'COLLEGE DETAILS', font = ('arial',25,'bold'), bg = 'orange')
       Label_1.grid(row = 0, column = 0, padx = 50, pady = 5)
       Label_2 = Label(Frame_2, text = 'STUDENT DETAILS', font = ('arial',25,'bold'), bg = 'orange')
       Label_2.grid(row = 0, column = 0, padx = 100, pady = 5)
       Label_3 = Label(Frame_3, text = 'EDIT CUTOFF VALUES', font = ('arial',25,'bold'), bg = 'orange')
       Label_3.grid(row = 0, column = 0, padx = 60, pady = 5)



       #BUTTONS
       Button_1 = Button(Frame_1, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __collegedetails__)
       Button_1.grid(row = 0, column = 3, padx = 50)
       Button_2 = Button(Frame_2, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __studdetails__)
       Button_2.grid(row = 0, column = 3, padx = 50)
       Button_3 = Button(Frame_3, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __cutoffdetails__)
       Button_3.grid(row = 0, column = 3, padx = 50)



       root.mainloop()


       

menu()
