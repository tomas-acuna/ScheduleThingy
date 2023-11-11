import sqlite3

con = sqlite3.connect("scheduleApp.db")
cur = con.cursor()

def adduser(name,password):
    cur.execute("INSERT INTO users VALUES(?,?)", [name,password])
    con.commit()

def addclass(clas,section,time):
    cur.execute("INSERT INTO classes VALUES(?,?,?)", [clas,section,time])
    con.commit()

def addclass_submission(name,clas,section):
    cur.execute("INSERT INTO class_submissions VALUES(?,?,?)",[name,clas,section])
    con.commit()

def fetchAllinClass(clas):
    hold = cur.execute("SELECT name FROM class_submissions WHERE class = ? ",[clas])
    return hold.fetchall()

def fetchAllinClassSection(clas,section):
    hold = cur.execute("SELECT name FROM class_submissions WHERE class = ? AND section = ? ",[clas,section])
    return hold.fetchall()

def getbio(name):
    hold = cur.execute("SELECT bio FROM user_bios WHERE name = ? ", [name])
    return hold.fetchall()

def getClasses(name):
    hold = cur.execute("SELECT class,section,professor,time FROM classes INNER JOIN class_submissions ON classes.class = class_submissions.class AND classes.section = class_submissions.section WHERE name = ? ", [name])
    return hold.fetchall()