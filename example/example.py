from book import Book
#   filename    classname
import booksSDK

# bookObj = Book("Are you my Mother?", 72)

# print(booksSDK.add_book(bookObj)) #prints returned ID of inserted record

# print(booksSDK.get_books()) #prints list of tuples -OR- book objects using __str__ as defined

# book = booksSDK.get_book_by_title('Are you my Mother?')

# print(type(book))

#instead of separate print and input we can use this:
#res = input("enter ur text\n")

while True:
    print("""
    Choose an option:
    1. print all books
    2. add a book
    3. update a book
    4. delete a book
    """)
    response = int(input())

    #there is no switch statement in python
    if response == 1:
        for book in booksSDK.get_books():
            print(book)
    elif response == 2:
        print("What is the name of the book?")
        title = input()
        print("How many pages is the book?")
        pages = int(input())

        book = Book(title, pages)
        booksSDK.add_book(book)
    elif response == 3:
        print("Current title ?")
        current_title = input()
        print("Current pages ?")
        current_pages = input()
        print("New title ?")
        new_title = input()
        print("New pages ?")
        new_pages = input()

        booksSDK.update_book(Book(current_title, current_pages), new_title, new_pages)
    elif response == 4:
        print("Title ?")
        title = input()
        print("Pages ?")
        pages = int(input())

        booksSDK.delete_book(Book(title, pages))
    else:
        print("Thanks for using our sweet app")
        break
