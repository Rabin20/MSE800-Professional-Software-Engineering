# main.py

from library import Library

# Create library instance
my_library = Library()

# Add some books
my_library.add_book("Harry Potter", "J.K. Rowling", 1997)
my_library.add_book("The Alchemist", "Paulo Coelho", 1988)

# Show all books
my_library.show_books()
