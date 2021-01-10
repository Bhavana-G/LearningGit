import sqlite3
from book import Book

def cursor():
    return sqlite3.connect('books.db').cursor()

c = cursor()
c.execute('CREATE TABLE IF NOT EXISTS books(title TEXT, pages INTEGER)')
c.connection.close()

def add_book(book):
    c = cursor()
    # c.execute('INSERT INTO books VALUES(?,?)', (book.title, book.pages))
    # c.connection.commit()
    # c.connection.close()
    #------OR-------
    with c.connection: #with will automatically commit
        c.execute('INSERT INTO books VALUES(?,?)', (book.title, book.pages))

    c.connection.close()
    return c.lastrowid #returns ID that was inserted

def get_books():
    c = cursor()

    # with c.connection:
    #     c.execute('SELECT * FROM books')
    
    # return c.fetchall() #returns list of tuples
    #-----------OR------------
    #return list of book objects
    books = []

    with c.connection:
        for book in c.execute('SELECT * FROM books'):
            books.append(Book(book[0], book[1]))

    c.connection.close()
    return books

def delete_book(book):
    c = cursor()
    with c.connection:
        c.execute("DELETE FROM books WHERE title=? AND pages=?", (book.title, book.pages))
    rows = c.rowcount
    c.connection.close()
    return rows

def update_book(book, new_title, new_pages):
    c = cursor()
    with c.connection:
        c.execute("UPDATE books SET title=?, pages=? WHERE title=? AND pages=?", 
        (new_title, new_pages, book.title, book.pages))
    book = get_book_by_title(book.title) #after commit
    c.connection.close()
    return book

def get_book_by_title(title):
    c = cursor()

    with c.connection:
        #concatenation with parameters risks for SQL injection
        #c.execute('SELECT * FROM books WHERE title = \"' + title + '\"')

        #so use ? (placeholder - pass a tuple to it) instead
        c.execute('SELECT * FROM books WHERE title = ?', (title,))

        # Python needs an additional comma in case of one element 
        # tuple to, differentiate between string and tuple.
        # It is only required for single-item tuples to disambiguate 
        # defining a tuple or an expression surrounded by parentheses. 
        # EX: a = ("s") is a string and
        # a = ("s",) is a tuple with one element.
        
        # For more than one item, it is no longer necessary 
        # since it is perfectly clear it is a tuple.
        # However, the trailing comma is allowed to make 
        # defining them using multiple lines easier. 
        # You could add to the end or rearrange items without 
        # breaking the syntax because you left out a comma on accident.
        # EX: a = [    1,    2,    3,     ]

        # Note that this applies to other collections 
        # (e.g., lists and dictionaries) too and not just tuples.
        # Summary: single-element tuples need a trailing comma, 
        # but it's optional for multiple-element tuples.
    
    data = c.fetchone()
    c.connection.close()

    if not data:
        return None
    
    return Book(data[0], data[1])
