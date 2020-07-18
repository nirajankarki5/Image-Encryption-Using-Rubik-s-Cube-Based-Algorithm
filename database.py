import sqlite3

def connect():
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS history (id INTEGER PRIMARY KEY, email text, date text)")
    conn.commit()
    conn.close()

def insert(email,date):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO history VALUES (NULL,?,?)",(email,date))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM history")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete():
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM history")
    conn.commit()
    conn.close()

connect()
