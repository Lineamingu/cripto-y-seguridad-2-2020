import sqlite3

conn = sqlite3.connect('hashes_4.sqlite')
cur = conn.cursor()
cur.execute('CREATE TABLE hash (content VARCHAR)')

f = open("hashes_descifrados_4.txt", "r")
ff = f.read()

for words in ff.split():
    cur.execute('INSERT INTO hash (content) VALUES (?)', ([words]))
    conn.commit()


f.close()

conn.close()