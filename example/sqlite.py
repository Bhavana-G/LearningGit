import sqlite3

conn = sqlite3.connect(":memory:") #creates new table each time we run - doesnt store anything

cur = conn.cursor()

cur.execute('CREATE TABLE books(title TEXT, pages INTEGER)')

#1st method - insert in only some particular columns
#cur.execute('''INSERT INTO books(title)
#                        VALUES("Are you my Mother?")''')

#2nd method - insert in same order as columns
cur.execute('INSERT INTO books VALUES("Are you my Mother?", 72)')
conn.commit() #commit for inserting to DB table

#3rd method - insert multiple values at a time
books = [
    ("Are you my Mother?", 72),
    ("The digging-est Dog", 72),
    ("The Giving Tree", 66)
]
cur.executemany('INSERT INTO books VALUES(?,?)', books) # ? - prevents SQL injection - works only for sequence of parameters in SQL query doesnt work in print string
conn.commit()

cur.execute('SELECT rowid, title FROM books WHERE title = "Are you my Mother?"')
data = cur.fetchall() #returns list of tuples
print(data)
#print('list=(?,?)', data)

cur.execute('SELECT * FROM books')
print(cur.fetchall())
#cur.execute('DELETE FROM books WHERE title = "Are you my Mother?"') #deletes both duplicates
#cur.execute('DELETE FROM books WHERE rowid = 2') #deletes one duplicate
#instead of deleting and re-inserting we can just update data in existing rows:
cur.execute('UPDATE books SET title = "New Book" WHERE rowid = 2')
conn.commit() #commit for deleting from DB table
cur.execute('SELECT * FROM books')
print(cur.fetchall())

