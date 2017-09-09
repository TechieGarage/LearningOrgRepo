import sqlite3

def createTable():
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE if not EXISTS Store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insertItem(item, quantity, price):
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Store VALUES(?,?,?)", (item, quantity, price))  # ? used to protect from sql injection
    conn.commit()
    conn.close()


insertItem("Bottle", 10, 50.5)

def viewTableData():
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Store")
    allRows = cur.fetchall()
    conn.close()
    return allRows


print(viewTableData())
