import sqlite3

conn = sqlite3.connect("users.db")
curs = conn.cursor()

curs.execute("SELECT * FROM users")
rows = curs.fetchall()

for row in rows:
    print(row)

conn.close()
