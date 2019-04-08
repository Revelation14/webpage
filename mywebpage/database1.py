import sqlite3

conn=sqlite3.connect("pythonweb.db")
cur=conn.cursor()
cur.execute(CREATE TABLE IF NOT EXISTS store1 (email STRING(50),password STRING(10),text TEXT))
conn.commit()
conn.close()

def insert():
    conn=sqlite3.connect("pythonweb.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store1 VALUES(%s,%s,%s,%s)",(email,password,text))
    conn.commit()
    conn.close()
