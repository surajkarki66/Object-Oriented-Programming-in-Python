import sqlite3
from typing import List,Dict,Union
# This is the basis that the database is used

#Book = Dict(str, Union(str,int))


def create_database() -> None:
    connections = sqlite3.connect('data.db') # connecting the database
    cursor = connections.cursor() # pointing the cursor to the top and move down

    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)') # Creathing the table in the database
    connections.commit() # To save in to the hardisk
    connections.close() # To close the server


def database_add(name: str, author: str) -> None:
    connections = sqlite3.connect('data.db')
    cursor = connections.cursor()
    try:
        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author,)) # Insert the top level value in the database
    except sqlite3.IntegrityError :
        print('The name already exist in database.')
    connections.commit()
    connections.close()
    


def get_list():
    connections = sqlite3.connect('data.db')
    cursor = connections.cursor()

    cursor.execute('SELECT * FROM books') # selecting the desired rows in the database
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

    connections.close()
    return books


def tick_book(name: str) -> None:
    connections = sqlite3.connect('data.db')
    cursor = connections.cursor()
    cursor.execute('SELECT name FROM books')
    # print(cursor.fetchall()) [('The Rocketing Nepal',), ('The Walking Death',), ('saman',)]
    name_list = [' '.join(item) for item in cursor.fetchall()] # Convert the tuples into the list of string
    # print(name_list) ['The Rocketing Nepal', 'The Walking Death', 'saman']
    for names in name_list:
        if names == name:
            cursor.execute(f"UPDATE books SET read=1 WHERE name=?", (name,))
            break
        elif names == name_list[-1]:# Compare the last value to the lastest value to print the else only once in the program
            print("Name Not found!")
    connections.commit()
    connections.close()


def delete_book(name: str) -> None:
    connections = sqlite3.connect('data.db')
    cursor = connections.cursor()

    cursor.execute('DELETE FROM books WHERE name=?', (name,))
    connections.commit()
    connections.close()

