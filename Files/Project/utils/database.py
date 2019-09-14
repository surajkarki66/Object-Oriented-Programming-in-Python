""" Concerned with storing and retrieving books from files"""

import json

books_file = 'books.json'

def create_book_table():
    with open(books_file,'w'):
        json.dump([],file,indent=2)

def add_book(name,author):
    books = get_all_books()
    books.append({'name':name, 'author': author ,'read': False})
    save_all_books(books)



def get_all_books():
   with open(books_file,'r') as file:
       return json.load(file)





def save_all_books(books):
    with open(books_file,'w') as file:
        json.dump(books,file,indent=2)






def mark_book_as_read(name):
    books = get_all_books()

    for book in books:
        if book['name'] == name:
            book['read'] = True

    save_all_books(books)

def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    save_all_books(books)









