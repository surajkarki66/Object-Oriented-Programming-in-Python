"""
    Get the input form the user and add them to the database

    1. Choice a to read book
    2. Choice l to list books
    3. Choice r to read books
    4. Choice d to delete books
    5. Choice q to quite the program
"""
import time
from utils import database
USER_CHOICE = """
        Choices:
        1. Choice a to read book
        2. Choice l to list books
        3. Choice r to read books
        4. Choice d to delete books
        5. Choice q to quite the program
        
        """

# for creathing the database


def get_books():
    database.create_database()
    choice = input(f'{USER_CHOICE}Enter Choice:')
    while choice!= 'q':
        if choice is 'a':
            add_book()
            time.sleep(2)
        elif choice is 'l':
            get_list_books()
            time.sleep(2)
        elif choice is 'r':
            read_book()
            time.sleep(2)
        elif choice is 'd':
            delete_book()
            time.sleep(2)
        else:
            print("Undefined choice!")
        choice = input(f'{USER_CHOICE}Enter Choice:')


def add_book():
    book_name = input('Enter the name of the book that you want to append:')
    book_author = input('The author of the book:')
    database.database_add(book_name, book_author)
    


def get_list_books():
    books = database.get_list()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']} is read: {read}")


def read_book():
    name = input('Enter the book you want to mark read:')
    database.tick_book(name)


def delete_book():
    name = input('Enter the name of the book to delete:')
    database.delete_book(name)
    print("The book is been deleted.")

get_books()
