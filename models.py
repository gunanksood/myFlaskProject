import sqlite3 as sql

def insertTable(title, content):
    con = sql.connect("content_table.db")
    cur = con.cursor()
    cur.execute("INSERT INTO content_table(title, content_text) VALUES (?, ?)", (title, content))
    con.commit()
    con.close()

def retrieveTable():
    con = sql.connect("content_table.db")
    cur = con.cursor()
    cur.execute("SELECT id, title, content_text FROM content_table")
    data = cur.fetchall()
    con.close()
    return data

def updateTable():
    con = sql.connect("content_table.db")
    cur = con.cursor()
    cur.execute("")
    data = cur.fetchall()
    con.close()
    return data