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

def updateTable(Id, Title, cont):
    con = sql.connect("content_table.db")
    cur = con.cursor()
    cur.execute("UPDATE content_table SET title = ?, content_text = ? WHERE id = ?",(Title, cont, Id,))
    con.commit()
    con.close()

def deleteData(id):
    con = sql.connect("content_table.db")
    cur = con.cursor()
    cur.execute("DELETE FROM content_table WHERE id = ?",(id,))
    con.commit()
    con.close()
