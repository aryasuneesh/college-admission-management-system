from tkinter import*
import tkinter.messagebox
import random
import Student_CutoffDisplay_Backend
from tkinter import ttk

master = Tk()

master.title('Cutoff Details')
master.geometry('1350x750')
master.config(bg = 'orange')


cutoff1 = StringVar()
cutoff2 = StringVar()
cutoff3 = StringVar()
cutoff4 = StringVar()
cutoff5 = StringVar()
cutoff6 = StringVar()

              
def StudentRec(event):
       try: 
              global selected_tuple
              
              index = listbox.curselection()[0]
              selected_tuple = listbox.get(index)

              Entry_cutoff1.delete(0, END)
              Entry_cutoff1.insert(END, selected_tuple[1])
              Entry_cutoff2.delete(0, END)
              Entry_cutoff2.insert(END, selected_tuple[2])
              Entry_cutoff3.delete(0, END)
              Entry_cutoff3.insert(END, selected_tuple[3])
              Entry_cutoff4.delete(0, END)
              Entry_cutoff4.insert(END, selected_tuple[4])
              Entry_cutoff5.delete(0, END)
              Entry_cutoff5.insert(END, selected_tuple[5])
              Entry_cutoff6.delete(0, END)
              Entry_cutoff6.insert(END, selected_tuple[6])

              
       except IndexError:
              pass


def Add():
       if(len(cutoff1.get()) != 0):
              Student_CutoffDisplay_Backend.insert(cutoff1.get(), cutoff2.get(), cutoff3.get(), cutoff4.get(), cutoff5.get(), cutoff6.get())
              listbox.delete(0, END)
              listbox.insert(END, (cutoff1.get(), cutoff2.get(), cutoff3.get(), cutoff4.get(), cutoff5.get(), cutoff6.get()))

def Display():
          listbox.delete(0, END)
          for row in Student_CutoffDisplay_Backend.view():
                 listbox.insert(END, row, str(' '))


def Exit():
       Exit = tkinter.messagebox.askyesno("Login System", "Confirm if you want to Exit")
       if Exit > 0:
              master.destroy()
              return 
       

def Reset():
       cutoff1.set('')
       cutoff2.set('')
       cutoff3.set('')
       cutoff4.set('')
       cutoff5.set('')
       cutoff6.set('')
       listbox.delete(0, END)



def Delete():
       if(len(cutoff1.get()) != 0):
          Student_CutoffDisplay_Backend.delete(selected_tuple[0])
          Reset()
          Display()


def Search():
       listbox.delete(0, END)
       for row in Student_CutoffDisplay_Backend.search(cutoff1.get(), cutoff2.get(), cutoff3.get(), cutoff4.get(), cutoff5.get(), cutoff6.get()):
              listbox.insert(END, row, str(' '))
              

def Update():
       if(len(cutoff1.get()) != 0):
          Student_CutoffDisplay_Backend.delete(selected_tuple[0])
       if(len(cutoff1.get()) != 0):
          Student_CutoffDisplay_Backend.insert(cutoff1.get(), cutoff2.get(), cutoff3.get(), cutoff4.get(), cutoff5.get(), cutoff6.get())

          listbox.delete(0, END)
          listbox.insert(END, (cutoff1.get(), cutoff2.get(), cutoff3.get(), cutoff4.get(), cutoff5.get(), cutoff6.get()))




Main_Frame = LabelFrame(master, width = 1300, height = 500, font = ('arial',20,'bold'), bg = 'DarkOrange1',bd = 15, relief = 'ridge')
Main_Frame.grid(row = 0, column = 0, padx = 10, pady = 20)

Frame_1 = LabelFrame(Main_Frame, width = 600, height = 400, font = ('arial',15,'bold'), \
                          relief = 'ridge', bd = 10, bg = 'DarkOrange1', text = 'CUTOFF DETAILS ')
Frame_1.grid(row = 1, column = 0, padx = 10)

Frame_2 = LabelFrame(Main_Frame, width = 750, height = 400, font = ('arial',15,'bold'), \
                          relief = 'ridge', bd = 10, bg = 'DarkOrange1', text = 'CUTOFF DATABASE')
Frame_2.grid(row = 1, column = 1, padx = 5)                  

Frame_3 = LabelFrame(master, width = 1200, height = 100, font = ('arial',10,'bold'), \
                          bg = 'DarkOrange1', relief = 'ridge', bd = 13)
Frame_3.grid(row = 2, column = 0, pady = 10)



Label_cutoff1 = Label(Frame_1, text = 'Cutoff for Integrated CSE', font = ('arial',20,'bold'),  bg = 'DarkOrange1')
Label_cutoff1.grid(row = 0, column = 0, sticky = W, padx = 20, pady = 10)
Label_cutoff2 = Label(Frame_1, text = 'Cutoff for Integrated ECE', font = ('arial',20,'bold'),  bg = 'DarkOrange1')
Label_cutoff2.grid(row = 1, column = 0, sticky = W, padx = 20)
Label_cutoff3 = Label(Frame_1, text = 'Cutoff for CSE', font = ('arial',20,'bold'),  bg = 'DarkOrange1')
Label_cutoff3.grid(row = 2, column = 0, sticky = W, padx = 20)
Label_cutoff4 = Label(Frame_1, text = 'Cutoff for ECE', font = ('arial',20,'bold'),  bg = 'DarkOrange1')
Label_cutoff4.grid(row = 3, column = 0, sticky = W, padx = 20)
Label_cutoff5 = Label(Frame_1, text = 'Cutoff for AE', font = ('arial',20,'bold'),  bg = 'DarkOrange1')
Label_cutoff5.grid(row = 4, column = 0, sticky = W, padx = 20)
Label_cutoff6 = Label(Frame_1, text = 'Cutoff for MCE', font = ('arial',20,'bold'),  bg = 'DarkOrange1')
Label_cutoff6.grid(row = 5, column = 0, sticky = W, padx = 20)




Entry_cutoff1 = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = cutoff1)
Entry_cutoff1.grid(row = 0, column = 1, padx = 10, pady = 5)
Entry_cutoff2 = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = cutoff2)
Entry_cutoff2.grid(row = 1, column = 1, padx = 10, pady = 5)
Entry_cutoff3 = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = cutoff3)
Entry_cutoff3.grid(row = 2, column = 1, padx = 10, pady = 5)
Entry_cutoff4 = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = cutoff4)
Entry_cutoff4.grid(row = 3, column = 1, padx = 10, pady = 5)
Entry_cutoff5 = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = cutoff5)
Entry_cutoff5.grid(row = 4, column = 1, padx = 10, pady = 5)
Entry_cutoff6 = Entry(Frame_1, font = ('arial',17,'bold'), textvariable = cutoff6)
Entry_cutoff6.grid(row = 5, column = 1, padx = 10, pady = 5)



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
btnExit = Button(Frame_3, text = 'EXIT', font = ('arial',17,'bold'), width = 8, command = Exit)
btnExit.grid(row = 0, column = 5, padx = 10, pady = 10)


scrollbar = Scrollbar(Frame_2)
scrollbar.grid(row = 0, column = 1, sticky = 'ns')

listbox = Listbox(Frame_2, width = 75, height = 20 , font = ('arial',12,'bold'))
listbox.bind('<<ListboxSelect>>', StudentRec)
listbox.grid(row = 0, column = 0)
scrollbar.config(command = listbox.yview)
              


master.mainloop()
