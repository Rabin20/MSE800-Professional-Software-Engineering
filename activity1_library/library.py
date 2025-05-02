# library.py

from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.books.append(new_book)

    def show_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nList of Books in the Library:")
            for book in self.books:
                book.display_info()
