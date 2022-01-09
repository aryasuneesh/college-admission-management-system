from tkinter import *
import sqlite3

def connect():
       conn = sqlite3.connect("collegeadmn.db")
       cur = conn.cursor()

       cur.execute("CREATE TABLE IF NOT EXISTS register (id integer PRIMARY KEY, username text, password text, confirm text)")

       conn.commit()
       conn.close()




def insert(username = ' ', password = ' ', confirm = ' '):
       con = sqlite3.connect('collegeadmn.db')
       cur = con.cursor()

       cur.execute('INSERT INTO register VALUES (NULL,?,?,?)',(username, password, confirm))

       con.commit()
       con.close()
       
def view():
       conn = sqlite3.connect("collegeadmn.db")
       cur = conn.cursor()

       cur.execute("SELECT * FROM register")
       rows = cur.fetchall()
       return rows

       conn.close()

connect()
