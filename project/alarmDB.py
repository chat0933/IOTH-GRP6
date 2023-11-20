import sqlite3
# Skriv ind i DB så snart der opstår et problem uanset om det er hjerte releateret eller om de er fladet

PATIENT_ID = 1
FALLEN = "TRUE"
HEARTH_RATE = 123
GPS1 = 666.666
GPS2 = 6969.6969


print("HEY")

database = ('plejehjem_database.db')

con = sqlite3.connect(database)
cur = con.cursor()

def create_patient_table():
    cur.execute('CREATE TABLE IF NOT EXISTS Issues(PATIENT_ID INT, FALLEN TEXT, HEARTH_RATE INT, GPS1 REAL, GPS2 REAL)')
    con.commit

def create_user_table():
    cur.execute('CREATE TABLE IF NOT EXISTS Users(uid INTEGER PRIMARY KEY,USERNAME TEXT, PASSWORD TEXT)')
    con.commit    

def create_user_account(username,password): #Use this function to save the created user from app.py into our database
    cur.execute('INSERT INTO users(username, password) VALUES (?, ?)', (username, password))
    con.commit

create_patient_table()
create_user_table()

def test_insert():
    username = "hejsa1"
    password = "test2"
    cur.execute('INSERT INTO Issues(PATIENT_ID, FALLEN, HEARTH_RATE, GPS1, GPS2) VALUES (?, ?, ?, ?, ?)', (PATIENT_ID,FALLEN, HEARTH_RATE,GPS1,GPS2))
    create_user_account(username,password)
    con.commit()
    cur.close()
    print("Inserted test into db")

test_insert()
