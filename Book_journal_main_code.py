import sqlite3

def create_database():
    conn = sqlite3.connect('TEST_book_journal.sqlite')
    c = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS books (ID INTEGER UNIQUE NOT NULL PRIMARY KEY, title TEXT, author TEXT, genre TEXT, year_published INTEGER, number_pages INTEGER, date_started DATE, date_ended DATE, rating INTEGER);"
    c.execute(query)

#FIX SYNTAX ERROR
def add_entry(title, author, genre, year_published, number_pages, date_started, date_ended, rating):
    conn = sqlite3.connect('TEST_book_journal.sqlite')
    c = conn.cursor()
    query = f"INSERT INTO books (ID, title, author, genre, year_published, number_pages, date_started, date_ended, rating) VALUES ({title},{author},{genre},{year_published},{number_pages},{date_started},{date_ended},{rating});"
    c.execute(query)
    conn.commit()
    conn.close()

def remove_entry(title, date_started):
    conn = sqlite3.connect('TEST_book_journal.sqlite')
    c = conn.cursor()
    query = f"DELETE FROM books where title = '{title}' AND date_started = {date_started};"
    c.execute(query)
    conn.commit()
    conn.close()

def view_books():
    conn = sqlite3.connect('TEST_book_journal.sqlite')
    c = conn.cursor()
    query = f"SELECT rowid, * FROM books;"
    c.execute(query)
    books = c.fetchall()
    return books


def view_title(title):
    conn = sqlite3.connect('TEST_book_journal.sqlite')
    c = conn.cursor()
    query = f"SELECT rowid, * FROM books where title = '{title}'"
    c.execute(query)
    books = c.fetchall()
    conn.close()
    return books

def view_author(author):
    conn = sqlite3.connect('TEST_book_journal.sqlite')
    c = conn.cursor()
    query = f"SELECT rowid, * FROM books where author = '{author}';"
    c.execute(query)
    books = c.fetchall()
    return books

def view_genre(genre):
    conn = sqlite3.connect('TEST_book_journal.sqlite')
    c = conn.cursor()
    query = f"SELECT rowid, * FROM books where genre = '{genre}'"
    c.execute(query)
    books = c.fetchall()
    return books

def view_year(year):
    conn = sqlite3.connect('TEST_book_journal.sqlite')
    c = conn.cursor()
    query = f"SELECT rowid, * FROM books where year_published = {year};"
    c.execute(query)
    books = c.fetchall()
    return books

def view_rating(rating):
    conn = sqlite3.connect('TEST_book_journal.sqlite')
    c = conn.cursor()
    query = f"SELECT rowid, * FROM books where rating = {rating};"
    c.execute(query)
    books = c.fetchall()
    return books

def update_book_string(title, start_date, data, new_data):
    conn = sqlite3.connect('TEST_book_journal.sqlite')
    c = conn.cursor()
    query = f"UPDATE books SET {data} = '{new_data}' WHERE title = '{title}' and start_date >= {start_date};"
    c.execute(query)
    conn.commit()
    conn.close()

def update_book_integer(title, start_date, data, new_data):
    conn = sqlite3.connect('TEST_book_journal.sqlite')
    c = conn.cursor()
    query = f"UPDATE books SET {data} = {new_data} WHERE title = '{title}' and start_date = {start_date};"
    c.execute(query)
    conn.commit()
    conn.close()

