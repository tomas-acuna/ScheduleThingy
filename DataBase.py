import sqlite3

con = sqlite3.connect("scheduleApp.db")
cur = con.cursor()
cur.execute("CREATE TABLE users(name,password)")