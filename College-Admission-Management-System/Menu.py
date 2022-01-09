from tkinter import*
import random
import os
import sys

def __Collegeapp__():
       filename = 'Student_reg_FrontEnd.py'
       os.system(filename)
       os.system('notepad'+filename)

def __Collegedet__():
       filename = 'Student_ViewDet_FrontEnd.py'
       os.system(filename)
       os.system('notepad'+filename)

def __CheckResult__():
       filename = 'Student_CutoffDisplay.py'
       os.system(filename)
       os.system('notepad'+filename)

 
def menu():
       root = Tk()
       root.title('Menu')
       root.geometry('1350x750')
       root.config(bg = 'orange')
       
       title_Frame = LabelFrame(root, font = ('arial',50,'bold'), width = 1000, height = 100, bg = 'DarkOrange1', relief = 'raise', bd = 13)
       title_Frame.grid(row = 0, column = 0, pady = 50)
       
       title_Label = Label(title_Frame, text = 'STUDENT MENU', font = ('arial',30,'bold'), bg = 'DarkOrange1')
       title_Label.grid(row = 0, column = 0, padx = 150)


       #Frames
       Frame_1 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'DarkOrange1', relief = 'ridge', bd = 10)
       Frame_1.grid(row = 1, column = 0, padx = 280)
       Frame_2 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'DarkOrange1', relief = 'ridge', bd = 10)
       Frame_2.grid(row = 2, column = 0, padx = 130, pady = 7)
       Frame_3 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'DarkOrange1', relief = 'ridge', bd = 10)
       Frame_3.grid(row = 3, column = 0, pady = 7)
  
       


       #Labels
       Label_1 = Label(Frame_1, text = 'COLLEGE APPLICATIONS', font = ('arial',25,'bold'), bg = 'DarkOrange1')
       Label_1.grid(row = 0, column = 0, padx = 50, pady = 5)
       Label_2 = Label(Frame_2, text = 'COLLEGE DETAILS', font = ('arial',25,'bold'), bg = 'DarkOrange1')
       Label_2.grid(row = 0, column = 0, padx = 100, pady = 5)
       Label_3 = Label(Frame_3, text = 'CHECK CUTOFF', font = ('arial',25,'bold'), bg = 'DarkOrange1')
       Label_3.grid(row = 0, column = 0, padx = 60, pady = 5)
       


       #Buttons
       Button_1 = Button(Frame_1, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __Collegeapp__)
       Button_1.grid(row = 0, column = 3, padx = 50)
       Button_2 = Button(Frame_2, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __Collegedet__)
       Button_2.grid(row = 0, column = 3, padx = 50)
       Button_3 = Button(Frame_3, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __CheckResult__)
       Button_3.grid(row = 0, column = 3, padx = 50)

       

       root.mainloop()


menu()
