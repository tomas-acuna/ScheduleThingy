import sqlite3

con = sqlite3.connect("scheduleApp.db")
cur = con.cursor()
cur.execute("CREATE TABLE users(name,password)")

cur.execute("CREATE TABLE class_submissions(name,class,section)")

cur.execute("CREATE TABLE classes(class,section,time)")

cur.execute("CREATE TABLE user_bios(name,bio)")






    