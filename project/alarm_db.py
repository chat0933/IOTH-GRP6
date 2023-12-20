import sqlite3

database = ('patient_database.db')

con = sqlite3.connect(database)
cur = con.cursor()

def create_user_table_chris():
    with sqlite3.connect("patient_database.db") as conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS Users(ID INTEGER PRIMARY KEY AUTOINCREMENT, USERNAME TEXT, PASSWORD TEXT)')
        con.commit

def create_issues_table_chris():
    with sqlite3.connect("patient_database.db") as conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS Issues(ID INTEGER PRIMARY KEY, FALLEN TEXT, HEARTH_RATE INTEGER, GPS1 REAL, GPS2 REAL)')
        con.commit
        
create_user_table_chris()
create_issues_table_chris()        