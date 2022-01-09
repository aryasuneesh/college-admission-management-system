import sqlite3

def connect():
       conn = sqlite3.connect("collegeadmn.db")
       cur = conn.cursor()

       cur.execute("CREATE TABLE IF NOT EXISTS studreg (id INTEGER PRIMARY KEY, name text, fname text, mname text, \
                     address text, mobno integer,email text, dob integer, gender text, eemarks float, scmarks float, prevsch text, firstpref text, secpref text )")

       conn.commit()
       conn.close()

def insert(name = " ", fname = " ", mname = " ", address = " ", mobno = " ", email = " ", dob = " ", gender = " ", eemarks=" ", scmarks=" ", prevsch=" ", firstpref = " ", secpref=" "):
       conn = sqlite3.connect("collegeadmn.db")
       cur = conn.cursor()

       cur.execute("INSERT INTO studreg VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?.?,?)", (name, fname, mname, address , mobno, email, dob, gender, eemarks, scmarks, prevsch, firstpref, secpref))

       conn.commit()
       conn.close()
                                                                        

def view():
       conn = sqlite3.connect("collegeadmn.db")
       cur = conn.cursor()

       cur.execute("SELECT * FROM studreg")
       rows = cur.fetchall()
       return rows

       conn.close()

def delete(id):
       conn = sqlite3.connect("collegeadmn.db")
       cur = conn.cursor()

       cur.execute("DELETE FROM studreg WHERE id = ?", (id))

       conn.commit()
       conn.close()

def update(id,name = " ", fname = " ", mname = " ", address = " ", mobno = " ", email = " ", dob = " ", gender = " ", eemarks=" ", scmarks=" ", prevsch=" ", firstpref = " ", secpref=" "):
       conn = sqlite3.connect("collegeadmn.db")
       cur = conn.cursor()

       cur.execute("UPDATE studreg SET name = ? OR fname = ? OR mname = ? OR address = ? OR mobno = ? OR email = ? OR dob = ? OR gender = ? OR eemarks = ? OR scmarks = ? OR prevsch = ? OR firstpref = ?  OR secpref = ?", (name, fname, mname, address , mobno, email, dob, gender, eemarks, scmarks, prevsch, firstpref, secpref))

       conn.commit()
       conn.close()

def search(name = " ", fname = " ", mname = " ", address = " ", mobno = " ", email = " ", dob = " ", gender = " ", eemarks=" ", scmarks=" ", prevsch=" ", firstpref = " ", secpref=" "):
       conn = sqlite3.connect("collegeadmn.db")
       cur = conn.cursor()

       cur.execute("SELECT * FROM studreg WHERE name = ? OR fname = ? OR mname = ? OR address = ? OR mobno = ? OR email = ? OR dob = ? OR gender = ? OR eemarks = ? OR scmarks = ? OR prevsch = ? OR firstpref = ?  OR secpref = ?", (name, fname, mname, address , mobno, email, dob, gender, eemarks, scmarks, prevsch, firstpref, secpref))
       rows = cur.fetchall()
       return rows
       
       conn.close()

                                                               
connect()
       
