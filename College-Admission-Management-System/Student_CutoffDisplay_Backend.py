import sqlite3

def connect():
       conn = sqlite3.connect("collegeadmn.db")
       cur = conn.cursor()

       cur.execute("CREATE TABLE IF NOT EXISTS cutoff (id INTEGER PRIMARY KEY, cutoff1 text, cutoff2 text, cutoff3 text, cutoff4 text, cutoff5 text, cutoff6 text)")
       conn.commit()
       conn.close()

def insert(cutoff1 = " ", cutoff2 = " ", cutoff3 = " ", cutoff4 = " ", cutoff5 = " ", cutoff6 = " "):
       conn = sqlite3.connect("collegeadmn.db")
       cur = conn.cursor()

       cur.execute("INSERT INTO cutoff VALUES (NULL,?,?,?,?,?,?)", (cutoff1, cutoff2 , cutoff3, cutoff4, cutoff5, cutoff6))

       conn.commit()
       conn.close()
                                                                        

def view():
       conn = sqlite3.connect("collegeadmn.db")
       cur = conn.cursor()

       cur.execute("SELECT * FROM cutoff")
       rows = cur.fetchall()
       return rows

       conn.close()

def delete(id):
       conn = sqlite3.connect("collegeadmn.db")
       cur = conn.cursor()

       cur.execute("DELETE FROM cutoff WHERE id = ?", (id,))

       conn.commit()
       conn.close()

def update(id,cutoff1 = " ", cutoff2 = " ", cutoff3 = " ", cutoff4 = " ", cutoff5 = " ", cutoff6 = " "):
       conn = sqlite3.connect("collegeadmn.db")
       cur = conn.cursor()

       cur.execute("UPDATE college SET cutoff1 = ? OR cutoff2 = ? OR cutoff3 = ? OR cutoff4 = ? OR cutoff5 = ? OR cutoff6 = ? ",(cutoff1, cutoff2 , cutoff3, cutoff4, cutoff5, cutoff6))

       conn.commit()
       conn.close()


                                                               
connect()
       
