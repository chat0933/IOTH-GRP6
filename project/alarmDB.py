import sqlite3

PATIENT_ID = 1
FALLEN = "TRUE"
HEARTH_RATE = 123
GPS1 = 666.666
GPS2 = 6969.6969

print("HEY")

database = ('patient_database.db')

con = sqlite3.connect(database)
cur = con.cursor()

def create_patient_table():
    cur.execute('CREATE TABLE IF NOT EXISTS Issues(PATIENT_ID INT, FALLEN TEXT, HEARTH_RATE INT, GPS1 REAL, GPS2 REAL)')

def create_user_table():
    cur.execute('CREATE TABLE IF NOT EXISTS Users(USERNAME TEXT, PASSWORD TEXT)')    

create_patient_table()
create_user_table()

def test_insert():
    cur.execute('INSERT INTO Issues(PATIENT_ID, FALLEN, HEARTH_RATE, GPS1, GPS2) VALUES (?, ?, ?, ?, ?)', (PATIENT_ID,FALLEN, HEARTH_RATE,GPS1,GPS2))
    con.commit()
    cur.close()
    print("Inserted test into db")

test_insert()

