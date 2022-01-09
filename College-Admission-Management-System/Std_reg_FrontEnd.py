from tkinter import *
import tkinter.messagebox  
import random
import Std_reg_BackEnd
from tkinter import ttk

master = Tk()

master = master
master.title('Student Information')
master.geometry('1350x735')
master.config(bg = 'orange')


studname = StringVar()
fname = StringVar()
mname = StringVar()
address = StringVar()
mobno = StringVar()
email = StringVar()
dob = StringVar()
gender = StringVar()
eemarks = StringVar()              # engineering exam marks
scmarks = StringVar()              # school marks
prevsch = StringVar()              # previous school
firstpref = StringVar()
secpref = StringVar()


def StudentRec(event):
  try: 
         global selected_tuple
         
         index = listbox.curselection()[0]
         selected_tuple = listbox.get(index)

         Entry_name.delete(0, END)
         Entry_name.insert(END, selected_tuple[0])
         Entry_fname.delete(0, END)
         Entry_fname.insert(END, selected_tuple[1])
         Entry_mname.delete(0, END)
         Entry_mname.insert(END, selected_tuple[2])
         Entry_address.delete(0, END)
         Entry_address.insert(END, selected_tuple[3])
         Entry_mobno.delete(0, END)
         Entry_mobno.insert(END, selected_tuple[4])
         Entry_emailID.delete(0, END)
         Entry_emailID.insert(END, selected_tuple[5])
         Entry_dob.delete(0, END)
         Entry_dob.insert(END, selected_tuple[6])
         Entry_gender.delete(0, END)
         Entry_gender.insert(END, selected_tuple[7])
         Entry_eemarks.delete(0, END)
         Entry_eemarks.insert(END, selected_tuple[8])
         Entry_scmarks.delete(0, END)
         Entry_scmarks.insert(END, selected_tuple[9])
         Entry_prevsch.delete(0, END)
         Entry_prevsch.insert(END, selected_tuple[10])
         Entry_firstpref.delete(0, END)
         Entry_firstpref.insert(END, selected_tuple[11])
         Entry_secpref.delete(0, END)
         Entry_secpref.insert(END, selected_tuple[12])
  except IndexError:
         pass

def Add():
  if(len(studname.get()) != 0):
     Std_reg_BackEnd.insert(studname.get(), fname.get(), mname.get(), address.get(), mobno.get(), email.get(), dob.get(), \
                             gender.get(), eemarks.get(), scmarks.get(), prevsch.get(), firstpref.get(), secpref.get())
     listbox.delete(0, END)
     listbox.insert(END, (studname.get(), fname.get(), mname.get(), address.get(), mobno.get(), email.get(), dob.get(), gender.get(), eemarks.get(), scmarks.get(), prevsch.get(), firstpref.get(), secpref.get()))
def Display():
     listbox.delete(0, END)
     for row in Std_reg_BackEnd.view():
            listbox.insert(END, row, str(' '))


def Exit():
    Exit = tkinter.messagebox.askyesno("Login System", "Confirm if you want to Exit")
    if Exit > 0:
           master.destroy()
           return 
  

def Reset():
    studname.set('')
    fname.set('')
    mname.set('')
    address.set('')
    mobno.set('')
    email.set('')
    dob.set('')
    gender.set('')
    eemarks.set('')
    scmarks.set('')
    prevsch.set('')
    firstpref.set('')
    secpref.set('')
    listbox.delete(0, END)



def Delete():
      if(len(studname.get()) != 0):
         Std_reg_BackEnd.py.delete(selected_tuple[0])
         Reset()
         Display()


def Search():
      listbox.delete(0, END)
      for row in Std_reg_BackEnd.search(studname.get(), fname.get(), mname.get(), address.get(), mobno.get(), email.get(), dob.get(),gender.get()):
             listbox.insert(END, row, str(' '))
             

def Update():
      if(len(studname.get()) != 0):
         Std_reg_BackEnd.delete(selected_tuple[0])
      if(len(studname.get()) != 0):
         Std_reg_BackEnd.insert(studname.get(), fname.get(), mname.get(), address.get(), mobno.get(), email.get(), dob.get(), \
                                 gender.get(), eemarks.get(), scmarks.get(), prevsch.get(), firstpref.get(), secpref.get())

         listbox.delete(0, END)
         listbox.insert(END, (studname.get(), fname.get(), mname.get(), address.get(), mobno.get(), email.get(), dob.get(), \
                                 gender.get(), eemarks.get(), scmarks.get(), prevsch.get(), firstpref.get(), secpref.get()))



#Frames

Main_Frame = LabelFrame(master, width = 1300, height = 700, font = ('Helvetica',25,'bold'), \
                            bg = 'DarkOrange1',bd = 5, relief = 'ridge')
Main_Frame.grid(row = 0, column = 0, padx = 10, pady = 20)

Frame_1 = LabelFrame(Main_Frame, width = 750, height = 620, font = ('Helvetica',20,'bold'), \
                         relief = 'ridge', bd = 5, bg = 'DarkOrange1', text = 'STUDENT INFORMATION ')
Frame_1.grid(row = 1, column = 0, padx = 15, pady = 30)

Frame_2 = LabelFrame(Main_Frame, width = 750, height = 620, font = ('Helvetica',20,'bold'), \
                         relief = 'ridge', bd = 5, bg = 'DarkOrange1', text = 'STUDENT DATABASE')
Frame_2.grid(row = 1, column = 1, padx = 15, pady = 30)                  

Frame_3 = LabelFrame(master, width = 1200, height = 80, font = ('Helvetica',10,'bold'), \
                         bg = 'DarkOrange1', relief = 'ridge', bd = 5)
Frame_3.grid(row = 2, column = 0, pady = 10)



#Labels of Frame_1
Label_name = Label(Frame_1, text = 'Student\'s name', font = ('arial',14,'bold'), bg = 'DarkOrange1')
Label_name.grid(row = 0, column = 0, sticky = W, padx = 20, pady = 10)
Label_fname = Label(Frame_1, text = 'Father\'s Name', font = ('arial',14,'bold'), bg = 'DarkOrange1')
Label_fname.grid(row = 1, column = 0, sticky = W, padx = 20)
Label_mname = Label(Frame_1, text = 'Mother\'s Name', font = ('arial',14,'bold'), bg = 'DarkOrange1')
Label_mname.grid(row = 2, column = 0, sticky = W, padx = 20)
Label_address = Label(Frame_1, text = 'Address', font = ('arial',14,'bold'),  bg = 'DarkOrange1')
Label_address.grid(row = 3, column = 0, sticky = W, padx = 20)
Label_mobno = Label(Frame_1, text = 'Mobile Number', font = ('arial',14,'bold'),  bg = 'DarkOrange1')
Label_mobno.grid(row = 4, column = 0, sticky = W, padx = 20)
Label_emailID = Label(Frame_1, text = 'Email ID', font = ('arial',14,'bold'),  bg = 'DarkOrange1')
Label_emailID.grid(row = 5, column = 0, sticky = W, padx = 20)
Label_dob = Label(Frame_1, text = 'Date of Birth', font = ('arial',14,'bold'),  bg = 'DarkOrange1')
Label_dob.grid(row = 6, column = 0, sticky = W, padx = 20)
Label_gender = Label(Frame_1, text = 'Gender', font = ('arial',14,'bold'),  bg = 'DarkOrange1')
Label_gender.grid(row = 7, column = 0, sticky = W, padx = 20, pady = 10)
Label_eemarks = Label(Frame_1, text = 'Entrance Exam Marks', font = ('arial',14,'bold'),  bg = 'DarkOrange1')
Label_eemarks.grid(row = 8, column = 0, sticky = W, padx = 20)
Label_scmarks = Label(Frame_1, text = 'Grade 12 Total Marks', font = ('arial',14,'bold'),  bg = 'DarkOrange1')
Label_scmarks.grid(row = 9, column = 0, sticky = W, padx = 20)
Label_prevsch = Label(Frame_1, text = 'Previous School', font = ('arial',14,'bold'),  bg = 'DarkOrange1')
Label_prevsch.grid(row = 10, column = 0, sticky = W, padx = 20)
Label_firstpref = Label(Frame_1, text = 'First Preferred Stream', font = ('arial',14,'bold'),  bg = 'DarkOrange1')
Label_firstpref.grid(row = 11, column = 0, sticky = W, padx = 20)
Label_secpref = Label(Frame_1, text = 'Second Preferred Stream', font = ('arial',14,'bold'),  bg = 'DarkOrange1')
Label_secpref.grid(row = 12, column = 0, sticky = W, padx = 20)


#Entries of Frame_1
Entry_name = Entry(Frame_1, font = ('arial',13,'bold'), textvariable = studname)
Entry_name.grid(row = 0, column = 1, padx = 10, pady = 5)
Entry_fname = Entry(Frame_1, font = ('arial',13,'bold'), textvariable = fname)
Entry_fname.grid(row = 1, column = 1, padx = 10, pady = 5)
Entry_mname = Entry(Frame_1, font = ('arial',13,'bold'), textvariable = mname)
Entry_mname.grid(row = 2, column = 1, padx = 10, pady = 5)
Entry_address = Entry(Frame_1, font = ('arial',13,'bold'), textvariable = address)
Entry_address.grid(row = 3, column = 1, padx = 10, pady = 5)
Entry_mobno = Entry(Frame_1, font = ('arial',13,'bold'), textvariable = mobno)
Entry_mobno.grid(row = 4, column = 1, padx = 10, pady = 5)
Entry_emailID = Entry(Frame_1, font = ('arial',13,'bold'), textvariable = email)
Entry_emailID.grid(row = 5, column = 1, padx = 10, pady = 5)
Entry_dob = Entry(Frame_1, font = ('arial',13,'bold'), textvariable = dob)
Entry_dob.grid(row = 6, column = 1, padx = 10, pady = 5)
Entry_gender = ttk.Combobox(Frame_1, values = (' ','Male','Female','Others'), font = ('arial',13,'bold'), textvariable = gender, width = 19)
Entry_gender.grid(row = 7, column = 1, padx = 10, pady = 5)
Entry_eemarks = Entry(Frame_1, font = ('arial',13,'bold'), textvariable = dob)
Entry_eemarks.grid(row = 8, column = 1, padx = 10, pady = 5)
Entry_scmarks = Entry(Frame_1, font = ('arial',13,'bold'), textvariable = eemarks)
Entry_scmarks.grid(row = 9, column = 1, padx = 10, pady = 5)
Entry_prevsch = Entry(Frame_1, font = ('arial',13,'bold'), textvariable = scmarks)
Entry_prevsch.grid(row = 10, column = 1, padx = 10, pady = 5)
Entry_firstpref = Entry(Frame_1, font = ('arial',13,'bold'), textvariable = firstpref)
Entry_firstpref.grid(row = 11, column = 1, padx = 10, pady = 5)
Entry_secpref = Entry(Frame_1, font = ('arial',13,'bold'), textvariable = secpref)
Entry_secpref.grid(row = 12, column = 1, padx = 10, pady = 5)




#Buttons of Frame_3
btnDisplay = Button(Frame_3, text = 'DISPLAY', font = ('arial',17,'bold'), width = 8, command = Display)
btnDisplay.grid(row = 0, column = 1, padx = 10, pady = 10)
btnReset = Button(Frame_3, text = 'RESET', font = ('arial',17,'bold'), width = 8, command = Reset)
btnReset.grid(row = 0, column = 2, padx = 10, pady = 10)
btnUpdate = Button(Frame_3, text = 'UPDATE', font = ('arial',17,'bold'), width = 8, command = Update)
btnUpdate.grid(row = 0, column = 3, padx = 10, pady = 10)
btnDelete = Button(Frame_3, text = 'DELETE', font = ('arial',17,'bold'), width = 8, command = Delete)
btnDelete.grid(row = 0, column = 4, padx = 10, pady = 10)
btnSearch = Button(Frame_3, text = 'SEARCH', font = ('arial',17,'bold'), width = 8, command = Search )
btnSearch.grid(row = 0, column = 5, padx = 10, pady = 10)
btnExit = Button(Frame_3, text = 'EXIT', font = ('arial',17,'bold'), width = 8, command = Exit)
btnExit.grid(row = 0, column = 6, padx = 10, pady = 10)



scrollbar = Scrollbar(Frame_2)
scrollbar.grid(row = 0, column = 1, sticky = 'ns')

listbox = Listbox(Frame_2, width = 75, height = 20 , font = ('arial',12,'bold'))
listbox.bind('<<ListboxSelect>>', StudentRec)
listbox.grid(row = 0, column = 0)
scrollbar.config(command = listbox.yview)

master.mainloop()
