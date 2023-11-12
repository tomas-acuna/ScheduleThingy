import sqlite3 
from schedule_parse import get_ics_info

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
    names = hold.fetchall()
    if len(names) == 0:
        return False
    return [name[0] for name in names]

def fetchAllinClassSection(clas,section):
    hold = cur.execute("SELECT name FROM class_submissions WHERE class = ? AND section = ? ",[clas,section])
    names = hold.fetchall()
    if len(names) == 0:
        return False
    return [name[0] for name in names]

def getbio(name):
    hold = cur.execute("SELECT bio FROM user_bios WHERE name = ? ", [name])
    bio = hold.fetchall()
    if len(bio) == 0:
        return False
    return bio[0][0]

def getClasses(name):
    hold = cur.execute("SELECT class,section,time FROM classes INNER JOIN class_submissions ON classes.class = class_submissions.class AND classes.section = class_submissions.section WHERE name = ? ", [name])
    list = hold.fetchall()
    if len(list) == 0:
        return False
    return list

def getPassword(name):
    hold = cur.execute("SELECT password FROM users WHERE name = ?", [name])
    password = hold.fetchall()
    if len(password) == 0:
        return False
    return password[0][0]

def createScheduleData(name,file):
    list = get_ics_info(file)
    
    for clas,section,time,days in list:

        res = " ".join([str(item) for item in days])
        time += res
        hold = cur.execute("SELECT class FROM classes WHERE EXISTS (SELECT class FROM classes WHERE class = ? AND section = ? AND time= ?) ",[clas,section,time])
        list = hold.fetchall()
        hold = cur.execute("SELECT class FROM class_submissions WHERE EXISTS (SELECT class FROM classes WHERE class = ? AND section = ? AND name= ?) ",[clas,section,name])
        if(len(list) == 0):
            addclass(clas,section,time)
        list = hold.fetchall()
        if(len(list) == 0):
            addclass_submission(name,clas,section)