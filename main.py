import sqlite3 as sq

with sq.connect("test.db") as con:
    cur=con.cursor()
    cur.execute("""CREATE TABLE users (name TEXT, sex INTEGER, old INTEGER, score INTEGER)""")
    con.commit()