from tkinter import*
import tkinter.messagebox
import random
import Clg_Details_BackEnd
from tkinter import ttk

master = Tk()

master.title('College Details')
master.geometry('1350x750')
master.config(bg = 'orange')


name = StringVar()
cno = StringVar()
ano = StringVar()
address = StringVar()
mobno = StringVar()
email = StringVar()
det = StringVar()
              
def StudentRec(event):
       try: 
              global selected_tuple
              
              index = listbox.curselection()[0]
              selected_tuple = listbox.get(index)

              Entry_name.delete(0, END)
              Entry_name.insert(END, selected_tuple[1])
              Entry_cno.delete(0, END)
              Entry_cno.insert(END, selected_tuple[2])
              Entry_ano.delete(0, END)
              Entry_ano.insert(END, selected_tuple[3])
              Entry_address.delete(0, END)
              Entry_address.insert(END, selected_tuple[4])
              Entry_mobno.delete(0, END)
              Entry_mobno.insert(END, selected_tuple[5])
              Entry_emailID.delete(0, END)
              Entry_emailID.insert(END, selected_tuple[6])
              Entry_det.delete(0, END)
              Entry_det.insert(END, selected_tuple[7])
              
       except IndexError:
              pass


def Add():
       if(len(name.get()) != 0):
              Clg_Details_BackEnd.insert(name.get(), cno.get(), ano.get(), address.get(), mobno.get(), email.get(), det.get())
              listbox.delete(0, END)
              listbox.insert(END, (name.get(), cno.get(), ano.get(), address.get(), mobno.get(), email.get(), det.get()))

def Display():
          listbox.delete(0, END)
          for row in Clg_Details_BackEnd.view():
                 listbox.insert(END, row, str(' '))


def Exit():
       Exit = tkinter.messagebox.askyesno("Login System", "Confirm if you want to Exit")
       if Exit > 0:
              master.destroy()
              return 
       

def Reset():
       name.set('')
       cno.set('')
       ano.set('')
       address.set('')
       mobno.set('')
       email.set('')
       det.set('')
       listbox.delete(0, END)



def Delete():
       if(len(name.get()) != 0):
          Clg_Details_BackEnd.delete(selected_tuple[0])
          Reset()
          Display()


def Search():
       listbox.delete(0, END)
       for row in Clg_Details_BackEnd.search(name.get(), cno.get(), ano.get(), address.get(), mobno.get(), email.get(), det.get()):
              listbox.insert(END, row, str(' '))
              

def Update():
       if(len(name.get()) != 0):
          Clg_Details_BackEnd.delete(selected_tuple[0])
       if(len(name.get()) != 0):
          Clg_Details_BackEnd.insert(name.get(), cno.get(), ano.get(), address.get(), mobno.get(), email.get(), det.get())

          listbox.delete(0, END)
          listbox.insert(END, (name.get(), cno.get(), ano.get(), address.get(), mobno.get(), email.get(), det.get()))




Main_Frame = LabelFrame(master, width = 1300, height = 500, font = ('arial',20,'bold'), bg = 'DarkOrange1',bd = 15, relief = 'ridge')
Main_Frame.grid(row = 0, column = 0, padx = 10, pady = 20)

Frame_1 = LabelFrame(Main_Frame, width = 600, height = 400, font = ('arial',15,'bold'), \
                          relief = 'ridge', bd = 10, bg = 'DarkOrange1', text = 'COLLEGE DETAILS ')
Frame_1.grid(row = 1, column = 0, padx = 10)

Frame_2 = LabelFrame(Main_Frame, width = 750, height = 400, font = ('arial',15,'bold'), \
                          relief = 'ridge', bd = 10, bg = 'DarkOrange1', text = 'COLLEGE DATABASE')
Frame_2.grid(row = 1, column = 1, padx = 5)                  

Frame_3 = LabelFrame(master, width = 1200, height = 100, font = ('arial',10,'bold'), \
                          bg = 'DarkOrange1', relief = 'ridge', bd = 13)
Frame_3.grid(row = 2, column = 0, pady = 10)



Label_name = Label(Frame_1, text = 'Name', font = ('arial',20,'bold'),  bg = 'DarkOrange1')
Label_name.grid(row = 0, column = 0, sticky = W, padx = 20, pady = 10)
Label_cno = Label(Frame_1, text = 'College Number', font = ('arial',20,'bold'),  bg = 'DarkOrange1')
Label_cno.grid(row = 1, column = 0, sticky = W, padx = 20)
Label_ano = Label(Frame_1, text = 'Affliation Number', font = ('arial',20,'bold'),  bg = 'DarkOrange1')
Label_ano.grid(row = 2, column = 0, sticky = W, padx = 20)
Label_address = Label(Frame_1, text = 'Address', font = ('arial',20,'bold'),  bg = 'DarkOrange1')
Label_address.grid(row = 3, column = 0, sticky = W, padx = 20)
Label_mobno = Label(Frame_1, text = 'Mobile Number', font = ('arial',20,'bold'),  bg = 'DarkOrange1')
Label_mobno.grid(row = 4, column = 0, sticky = W, padx = 20)
Label_emailID = Label(Frame_1, text = 'Email ID', font = ('arial',20,'bold'),  bg = 'DarkOrange1')
Label_emailID.grid(row = 5, column = 0, sticky = W, padx = 20)
Label_det = Label(Frame_1, text = 'Details', font = ('arial',20,'bold'),  bg = 'DarkOrange1')
Label_det.grid(row = 6, column = 0, sticky = W, padx = 20, pady = 70)



Entry_name = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = name)
Entry_name.grid(row = 0, column = 1, padx = 10, pady = 5)
Entry_cno = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = cno)
Entry_cno.grid(row = 1, column = 1, padx = 10, pady = 5)
Entry_ano = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = ano)
Entry_ano.grid(row = 2, column = 1, padx = 10, pady = 5)
Entry_address = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = address)
Entry_address.grid(row = 3, column = 1, padx = 10, pady = 5)
Entry_mobno = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = mobno)
Entry_mobno.grid(row = 4, column = 1, padx = 10, pady = 5)
Entry_emailID = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = email)
Entry_emailID.grid(row = 5, column = 1, padx = 10, pady = 5)
Entry_dob = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = det)
Entry_dob.grid(row = 6, column = 1, padx = 10, pady = 50)





btnSave = Button(Frame_3, text = 'SAVE', font = ('arial',17,'bold'), width = 8, command = Add)
btnSave.grid(row = 0, column = 0, padx = 10, pady = 10)
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
