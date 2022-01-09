from tkinter import*
import tkinter.messagebox
import random
import Student_reg_BackEnd
from tkinter import ttk

master = Tk()
master.title('Student Information')
master.geometry('1350x750')
master.config(bg = 'orange')


name = StringVar()
fname = StringVar()
mname = StringVar()
address = StringVar()
mobno = StringVar()
email = StringVar()
dob = StringVar()
gender = StringVar()
eemarks = StringVar()                                  
scmarks = StringVar()                                  
prevsch = StringVar()                                   
firstpref = StringVar()
secpref = StringVar()


def StudentRec(event):
       try: 
              global selected_tuple
              
              index = listbox.curselection()[0]
              selected_tuple = listbox.get(index)

              Entry_name.delete(0, END)
              Entry_name.insert(END, selected_tuple[1])
              Entry_fname.delete(0, END)
              Entry_fname.insert(END, selected_tuple[2])
              Entry_mname.delete(0, END)
              Entry_mname.insert(END, selected_tuple[3])
              Entry_address.delete(0, END)
              Entry_address.insert(END, selected_tuple[4])
              Entry_mobno.delete(0, END)
              Entry_mobno.insert(END, selected_tuple[5])
              Entry_emailID.delete(0, END)
              Entry_emailID.insert(END, selected_tuple[6])
              Entry_dob.delete(0, END)
              Entry_dob.insert(END, selected_tuple[7])
              Entry_gender.delete(0, END)
              Entry_gender.insert(END, selected_tuple[8])
              Entry_eemarks.delete(0, END)
              Entry_eemarks.insert(END, selected_tuple[9])
              Entry_scmarks.delete(0, END)
              Entry_scmarks.insert(END, selected_tuple[10])
              Entry_prevsch.delete(0, END)
              Entry_prevsch.insert(END, selected_tuple[11])
              Entry_firstpref.delete(0, END)
              Entry_firstpref.insert(END, selected_tuple[12])
              Entry_secpref.delete(0, END)
              Entry_secpref.insert(END, selected_tuple[13])
       except IndexError:
              pass



def Add():
       if(len(name.get()) != 0):
          Student_reg_BackEnd.insert(name.get(), fname.get(), mname.get(), address.get(), mobno.get(), email.get(), dob.get(), \
                                  gender.get(), eemarks.get(), scmarks.get(), prevsch.get(), firstpref.get(), secpref.get())
          listbox.delete(0, END)
          listbox.insert(END, (name.get(), fname.get(), mname.get(), address.get(), mobno.get(), email.get(), dob.get(), gender.get(), eemarks.get(), scmarks.get(), prevsch.get(), firstpref.get(), secpref.get()))
def Display():
          listbox.delete(0, END)
          
          for row in Student_reg_BackEnd.view():
                 listbox.insert(END, row, str(' '))


def Exit():
       Exit = tkinter.messagebox.askyesno("Login System", "Confirm if you want to Exit")
       if Exit > 0:
              master.destroy()
              return 
       

def Reset():
       name.set('')
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



def Update():
       if(len(name.get()) != 0):
          Student_reg_BackEnd.delete(selected_tuple[0])
       if(len(name.get()) != 0):
          Student_reg_BackEnd.insert(name.get(), fname.get(), mname.get(), address.get(), mobno.get(), email.get(), dob.get(), \
                                  gender.get(), eemarks.get(), scmarks.get(), prevsch.get(), firstpref.get(), secpref.get())

          listbox.delete(0, END)
          listbox.insert(END, (name.get(), fname.get(), mname.get(), address.get(), mobno.get(), email.get(), dob.get(), \
                                  gender.get(), eemarks.get(), scmarks.get(), prevsch.get(), firstpref.get(), secpref.get()))




Main_Frame = LabelFrame(master, width = 1300, height = 700, font = ('arial',20,'bold'), \
                             bg = 'orange',bd = 5, relief = 'ridge')
Main_Frame.grid(row = 0, column = 0, padx = 10, pady = 20)

Frame_1 = LabelFrame(Main_Frame, width = 1250, height = 620, font = ('arial',15,'bold'), \
                          relief = 'ridge', bd = 0, bg = 'orange', text = 'STUDENT INFORMATION ')
Frame_1.grid(row = 1, column = 0, padx = 335, pady = 10)
                

Frame_3 = LabelFrame(master, width = 1200, height = 80, font = ('arial',10,'bold'), \
                          bg = 'orange', relief = 'ridge', bd = 5)
Frame_3.grid(row = 2, column = 0, pady = 10)



#========================================================Labels of Frame_1========================================================
Label_name = Label(Frame_1, text = 'Student\'s name', font = ('arial',14,'bold'),  bg = 'orange')
Label_name.grid(row = 0, column = 0, sticky = W, padx = 50, pady = 10)
Label_fname = Label(Frame_1, text = 'Father\'s Name', font = ('arial',14,'bold'),  bg = 'orange')
Label_fname.grid(row = 1, column = 0, sticky = W, padx = 50)
Label_mname = Label(Frame_1, text = 'Mother\'s Name', font = ('arial',14,'bold'),  bg = 'orange')
Label_mname.grid(row = 2, column = 0, sticky = W, padx = 50)
Label_address = Label(Frame_1, text = 'Address', font = ('arial',14,'bold'),  bg = 'orange')
Label_address.grid(row = 3, column = 0, sticky = W, padx = 50)
Label_mobno = Label(Frame_1, text = 'Mobile Number', font = ('arial',14,'bold'),  bg = 'orange')
Label_mobno.grid(row = 4, column = 0, sticky = W, padx = 50)
Label_emailID = Label(Frame_1, text = 'Email ID', font = ('arial',14,'bold'),  bg = 'orange')
Label_emailID.grid(row = 5, column = 0, sticky = W, padx = 50)
Label_dob = Label(Frame_1, text = 'Date of Birth', font = ('arial',14,'bold'),  bg = 'orange')
Label_dob.grid(row = 6, column = 0, sticky = W, padx = 50)
Label_gender = Label(Frame_1, text = 'Gender', font = ('arial',14,'bold'),  bg = 'orange')
Label_gender.grid(row = 7, column = 0, sticky = W, padx = 50, pady = 10)
Label_eemarks = Label(Frame_1, text = 'Entrance Exam Marks', font = ('arial',14,'bold'),  bg = 'orange')
Label_eemarks.grid(row = 8, column = 0, sticky = W, padx = 50)
Label_scmarks = Label(Frame_1, text = 'Grade 12 Total Marks', font = ('arial',14,'bold'),  bg = 'orange')
Label_scmarks.grid(row = 9, column = 0, sticky = W, padx = 50)
Label_prevsch = Label(Frame_1, text = 'Previous School', font = ('arial',14,'bold'),  bg = 'orange')
Label_prevsch.grid(row = 10, column = 0, sticky = W, padx = 50)
Label_firstpref = Label(Frame_1, text = 'First Preferred Stream', font = ('arial',14,'bold'),  bg = 'orange')
Label_firstpref.grid(row = 11, column = 0, sticky = W, padx = 50)
Label_secpref = Label(Frame_1, text = 'Second Preferred Stream', font = ('arial',14,'bold'),  bg = 'orange')
Label_secpref.grid(row = 12, column = 0, sticky = W, padx = 50)


#========================================================Entries of Frame_1========================================================
Entry_name = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = name)
Entry_name.grid(row = 0, column = 1, padx = 50, pady = 5)
Entry_fname = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = fname)
Entry_fname.grid(row = 1, column = 1, padx = 50, pady = 5)
Entry_mname = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = mname)
Entry_mname.grid(row = 2, column = 1, padx = 50, pady = 5)
Entry_address = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = address)
Entry_address.grid(row = 3, column = 1, padx = 50, pady = 5)
Entry_mobno = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = mobno)
Entry_mobno.grid(row = 4, column = 1, padx = 50, pady = 5)
Entry_emailID = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = email)
Entry_emailID.grid(row = 5, column = 1, padx = 50, pady = 5)
Entry_dob = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = dob)
Entry_dob.grid(row = 6, column = 1, padx = 50, pady = 5)
Entry_gender = ttk.Combobox(Frame_1, values = (' ','Male','Female','Others'), font = ('arial',17,'bold'), textvariable = gender, width = 19)
Entry_gender.grid(row = 7, column = 1, padx = 50, pady = 5)
Entry_eemarks = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = eemarks)
Entry_eemarks.grid(row = 8, column = 1, padx = 50, pady = 5)
Entry_scmarks = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = scmarks)
Entry_scmarks.grid(row = 9, column = 1, padx = 50, pady = 5)
Entry_prevsch = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = prevsch)
Entry_prevsch.grid(row = 10, column = 1, padx = 50, pady = 5)
Entry_firstpref = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = firstpref)
Entry_firstpref.grid(row = 11, column = 1, padx = 50, pady = 5)
Entry_secpref = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = secpref)
Entry_secpref.grid(row = 12, column = 1, padx = 50, pady = 5)




#========================================================Buttons of Frame_3=========================================================
btnSave = Button(Frame_3, text = 'SAVE', font = ('arial',17,'bold'), width = 8, command = Add)
btnSave.grid(row = 0, column = 0, padx = 10, pady = 10)
btnReset = Button(Frame_3, text = 'RESET', font = ('arial',17,'bold'), width = 8, command = Reset)
btnReset.grid(row = 0, column = 1, padx = 10, pady = 10)
btnUpdate = Button(Frame_3, text = 'UPDATE', font = ('arial',17,'bold'), width = 8, command = Update)
btnUpdate.grid(row = 0, column = 2, padx = 10, pady = 10)
btnExit = Button(Frame_3, text = 'EXIT', font = ('arial',17,'bold'), width = 8, command = Exit)
btnExit.grid(row = 0, column = 3, padx = 10, pady = 10)

master.mainloop()

              

     

