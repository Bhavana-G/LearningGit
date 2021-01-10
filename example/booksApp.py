import tkinter
from tkinter import END
from book import Book
import booksSDK

books = [] #used for finding the book to delete -OR- make new method in booksSDK to delete by title or ID

def add_to_list():
    book = Book(title_entry.get(), pages_entry.get())
    if(booksSDK.add_book(book)):
        books.append(book)
        listbox.insert(END, book)
        title_entry.delete(0, END)
        pages_entry.delete(0, END)

def remove_from_list():
    book_tuple = listbox.curselection() #returns single element tuple with the position of the selected list item
    book = books.pop(book_tuple[0]) #selecting first element of the tuple
    if(booksSDK.delete_book(book)):
        listbox.delete(book_tuple)

tk = tkinter.Tk()
tk.title("Books App")

listbox = tkinter.Listbox(tk)
listbox.pack()

for book in booksSDK.get_books():
    books.append(book)
    listbox.insert(END, book)

title = tkinter.Label(tk, text="Book Title:")
title.pack()
title_entry = tkinter.Entry(tk)
title_entry.pack()

pages = tkinter.Label(tk, text="No of Pages:")
pages.pack()
pages_entry = tkinter.Entry(tk)
pages_entry.pack()

tkinter.Button(tk, text="Add Book", command=add_to_list).pack()
tkinter.Button(tk, text="Remove Selected Book", command=remove_from_list).pack()

tk.mainloop()
