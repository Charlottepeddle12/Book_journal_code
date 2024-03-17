from dataclasses import dataclass
from datetime import datetime
import Book_journal_main_code as MC
import time

@dataclass
class Book:
    def __init__(self, title:str="", author:str="", genre:str="", year_published:int=0, number_pages:int=0, date_started:datetime=datetime.now(), date_finished:datetime=datetime.now(), rating:int=0):
        self.title = title
        self.author = author
        self.genre = genre
        self.year_published = year_published
        self.number_pages = number_pages
        self.date_started = date_started
        self.date_finished = date_finished
        self.rating = rating

    @property
    def get_title(self):
        return self.title

    @property
    def get_author(self):
        return self.author

    @property
    def get_genre(self):
        return self.genre

    @property
    def get_year_published(self):
        return self.year_published

    @property
    def get_number_pages(self):
        return self.number_pages

    @property
    def get_date_started(self):
        return self.date_started

    @property
    def get_date_finished(self):
        return self.date_finished

    @property
    def get_rating(self):
        return self.rating

    @get_title.setter
    def get_title(self, value):
        self.title = value

    @get_author.setter
    def get_author(self, value):
        self.author = value

    @get_genre.setter
    def get_genre(self, value):
        self.genre = value

    @get_year_published.setter
    def get_year_published(self, value):
        if self.year_published < 1300:
            raise ValueError("YEAR CANNOT BE BELOW 1300.")
        else:
            self.year_published = value

    @get_number_pages.setter
    def get_number_pages(self, value):
        if self.number_pages < 0:
            raise ValueError("NUMBER OF PAGES CANNOT BE BELOW 0.")
        else:
            self.number_pages = value

    @get_date_started.setter
    def get_date_started(self, value):
        format = "%Y-%m-%d"
        self.date_started = datetime.strptime(value, format)

    @get_date_finished.setter
    def get_date_finished(self, value):
        format = "%Y-%m-%d"
        self.date_finished = datetime.strptime(value, format)

    @get_rating.setter
    def get_rating(self, value):
        if value < 0 or value > 6:
            raise ValueError("RATING CANNOT BE BELOW 0 OR ABOVE 6.")
        else:
            self.rating = value

#THINGS TO ADD:
    #- ADD METHOD TO ORDER BOOKS IN ALPHABETICAL, BY YEAR, RATING, DATES, ETC...
    #- ADD METHOD SHOW HOW MANY TIMES A BOOK WAS READ
    #- ADD A TABLE FOR BOOKS CURRENTLY READING
    #- ADD TABLE FOR SERIES
    #- ADD SERIES ID FOR BOOKS
    #- UPDATE GENRE METHOD SO IT LOOKS FOR WORDS WITHIN THE STRING FOR GENRE METHOD
    #- ADD MESSAGE IF SOMETHING IS NOT PRESENT IN DATABASE
    #- FIX SO VIEW_BY_YEAR SHOWS THE YEAR READ AND NOT YEAR PUBLISHED

    def add_book(self): #TEST
        while True:
            try:
                title = input("Title of book: ").title()
                author = input("Author: ").title()
                genre = input("Genre: ").title()
                year_published = int(input("Year published: "))
                number_pages = int(input("Number of pages: "))
                date_started = input("Date started: ")
                date_finished = input("Date finished: ")
                rating = int(input("Rating: "))
                MC.add_entry(title, author, genre, year_published, number_pages, date_started, date_finished, rating)
                print(f"{title} was added!")
                break
            except ValueError as e:
                print(e)

    def remove_entry(self): #TEST
        while True:
            try:
                title = input("Title of book you wan to delete: ")
                date_started = input("Date started: ")
                MC.remove_entry(title, date_started)
                print(f"{title} was removed.")
            except ValueError as e:
                print(e)

    def view_book(self):
        while True:
            try:
                books = MC.view_books()
                for book in books:
                    print("==========")
                    print(f"ID: {book[0]}\nTITLE: {book[1]}\nAUTHOR: {book[2]}\nGENRE: {book[3]}\nYEAR PUBLISHED: {book[4]}\nNUMBER OF PAGES: {book[5]}\nDATE STARTED: {book[6]}\nDATE FINISHED: {book[7]}\nRATING: {book[8]}")
                print("==========")
                break
            except ValueError as e:
                print(e)

    def view_by_title(self):
        while True:
            try:
                title = input("Title of book: ").title()
                books = MC.view_title(title)
                for book in books:
                    print("==========")
                    print(f"ID: {book[0]}\nTITLE: {book[1]}\nAUTHOR: {book[2]}\nGENRE: {book[3]}\nYEAR PUBLISHED: {book[4]}\nNUMBER OF PAGES: {book[5]}\nDATE STARTED: {book[6]}\nDATE FINISHED: {book[7]}\nRATING: {book[8]}")
                print("==========")
                break
            except ValueError as e:
                print(e)

    def view_by_author(self):
        while True:
            try:
                author = input("Author name: ").title()
                books = MC.view_author(author)
                for book in books:
                    print("==========")
                    print(f"ID: {book[0]}\nTITLE: {book[1]}\nAUTHOR: {book[2]}\nGENRE: {book[3]}\nYEAR PUBLISHED: {book[4]}\nNUMBER OF PAGES: {book[5]}\nDATE STARTED: {book[6]}\nDATE FINISHED: {book[7]}\nRATING: {book[8]}")
                print("==========")
                break
            except ValueError as e:
                print(e)

    def view_by_genre(self):
        while True:
            try:
                genre = input("Genre: ").title()
                books = MC.view_genre(genre)
                for book in books:
                    print("==========")
                    print(f"ID: {book[0]}\nTITLE: {book[1]}\nAUTHOR: {book[2]}\nGENRE: {book[3]}\nYEAR PUBLISHED: {book[4]}\nNUMBER OF PAGES: {book[5]}\nDATE STARTED: {book[6]}\nDATE FINISHED: {book[7]}\nRATING: {book[8]}")
                print("==========")
                break
            except ValueError as e:
                print(e)

    def view_by_year(self):
        while True:
            try:
                year = int(input("Year: "))
                books = MC.view_year(year)
                for book in books:
                    print("==========")
                    print(f"ID: {book[0]}\nTITLE: {book[1]}\nAUTHOR: {book[2]}\nGENRE: {book[3]}\nYEAR PUBLISHED: {book[4]}\nNUMBER OF PAGES: {book[5]}\nDATE STARTED: {book[6]}\nDATE FINISHED: {book[7]}\nRATING: {book[8]}")
                print("==========")
                break
            except ValueError as e:
                print(e)

    def view_by_rating(self):
        while True:
            try:
                rating = int(input("Rating: "))
                books = MC.view_rating(rating)
                for book in books:
                    print("\n==========")
                    print(f"ID: {book[0]}\nTITLE: {book[1]}\nAUTHOR: {book[2]}\nGENRE: {book[3]}\nYEAR PUBLISHED: {book[4]}\nNUMBER OF PAGES: {book[5]}\nDATE STARTED: {book[6]}\nDATE FINISHED: {book[7]}\nRATING: {book[8]}")
                print("==========")
                break
            except ValueError as e:
                print(e)

    def edit_entry(self): #TEST
        while True:
            try:
                data = input("What do you wish to change?: title, author, genre, number_pages, rating").lower()
                if data == "title" or data == "author" or data == "genre":
                    title = input("What book do you wish to change?: ").title()
                    start_date = input(f"What is the start date of {title}?: ")
                    new_data = input(f'WHat will be the new {data} for {title}?: ').title()
                    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
                    MC.update_book_string(title, start_date, data, new_data)
                    print(f"{title}'s {data} was changed to {new_data}.")
                elif data == "number_pages" or data == "rating":
                    title = input("What book do you wish to change?: ").title()
                    start_date = input(f"What is the start date of {title}?: ")
                    new_data = int(input(f'What will be the new {data} for {title: }?'))
                    MC.update_book_integer(title, start_date, data, new_data)
                    print(f"{title}'s {data} was changed to {new_data}.")
                else:
                    print("Invalid option. Try again")
                    print("If editing the number of pages, input 'number_pages' and not 'number pages'.")
            except ValueError as e:
                print(e)


def menu():
    print("1. Add book")
    print("2. Delete entry")
    print("3. View all books")
    print("4. View by title")
    print("5. View by author")
    print("6. View by genre")
    print("7. View by year")
    print("8. View by rating")
    print("9. Edit book")
    print("10. Exit")

def choice():
    try:
        while True:
            choice = int(input("\nCommand: "))
            return choice
    except ValueError:
        print("Invalid. Must be Integer.")

def main():
    book = Book()
    menu()
    go = "y"
    while go == "y":
        user_choice = choice()
        if user_choice == 1:
            book.add_book()
        elif user_choice == 2:
            book.remove_entry()
        elif user_choice == 3:
            book.view_book()
        elif user_choice == 4:
            book.view_by_title()
        elif user_choice == 5:
            book.view_by_author()
        elif user_choice == 6:
            book.view_by_genre()
        elif user_choice == 7:
            book.view_by_year()
        elif user_choice == 8:
            book.view_by_rating()
        elif user_choice == 9:
            book.edit_entry()
        elif user_choice == 10:
            print("Exiting...")
            time.sleep(1.5)
            break
        else:
            print("Invalid choice. Try again.")
            menu()

if __name__ == "__main__":
    MC.create_database()
    main()
    print("\nProgram exited.")


