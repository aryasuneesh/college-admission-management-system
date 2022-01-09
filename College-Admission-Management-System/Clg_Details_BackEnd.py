import sqlite3

def connect():
       conn = sqlite3.connect("collegeadmn.db")
       cur = conn.cursor()

       cur.execute("CREATE TABLE IF NOT EXISTS college (id INTEGER PRIMARY KEY, name text, cno text, ano text, address text, mobno integer, email text, det integer)")

       conn.commit()
       conn.close()

def insert(name = " ", cno = " ", ano = " ", address = " ", mobno = " ", email = " ", det = " "):
       conn = sqlite3.connect("collegeadmn.db")
       cur = conn.cursor()

       cur.execute("INSERT INTO college VALUES (NULL,?,?,?,?,?,?,?)", (name, cno, ano, address , mobno, email, det))

       conn.commit()
       conn.close()
                                                                        

def view():
       conn = sqlite3.connect("collegeadmn.db")
       cur = conn.cursor()

       cur.execute("SELECT * FROM college")
       rows = cur.fetchall()
       return rows

       conn.close()

def delete(id):
       conn = sqlite3.connect("collegeadmn.db")
       cur = conn.cursor()

       cur.execute("DELETE FROM college WHERE id = ?", (id,))

       conn.commit()
       conn.close()

def update(id,name = " ", cno = " ", ano = " ", address = " ", mobno = " ", email = " ", dob = " "):
       conn = sqlite3.connect("collegeadmn.db")
       cur = conn.cursor()

       cur.execute("UPDATE college SET name = ? OR cno = ? OR ano = ? OR address = ? OR mobno = ? OR email = ? OR det = ?",(name, cno, ano, address , mobno, email, det))

       conn.commit()
       conn.close()

def search(name = " ", cno = " ", ano = " ", address = " ", mobno = " ", email = " ", det = " "):
       conn = sqlite3.connect("collegeadmn.db")
       cur = conn.cursor()

       cur.execute("SELECT * FROM college WHERE name = ? OR cno = ? OR ano = ? OR address = ? OR mobno = ? OR email = ? OR det = ?", (name, cno, ano, address , mobno, email, det))
       rows = cur.fetchall()
       return rows
       
       conn.close()

                                                               
connect()
       
