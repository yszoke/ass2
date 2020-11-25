import sqlite3

"""Creating a connection"""
conn = sqlite3.connect('lite.db')

"""Creating a cursor object"""
cur = conn.cursor()

"""Performing a query, commit and close"""
cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT,quantity INTEGER,price REAL)")
conn.commit()
conn.close()

def view():
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM store;")
    rows=cur.fetchall()
    for row in rows:
        print (row )
