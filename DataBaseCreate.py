import sqlite3
import os

if __name__ == "__main__":

    if os.path.exists("scheduleApp.db"):
        os.remove("scheduleApp.db")

    con = sqlite3.connect("scheduleApp.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE users(name,password)")

    cur.execute("CREATE TABLE class_submissions(name,class,section)")

    cur.execute("CREATE TABLE classes(class,section,time)")

    cur.execute("CREATE TABLE user_bios(name,bio)")
