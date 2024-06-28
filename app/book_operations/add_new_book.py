from app.classes.book import Book
def new_book():
    Book()
    title = input("Enter the title of the book:\n").title()
    author = input("Enter the name of the author for the book")