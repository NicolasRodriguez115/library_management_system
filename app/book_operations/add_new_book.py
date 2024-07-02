from app.classes.book import Book
from app.classes.author import authors
def new_book():
    title = input("Enter the title of the book:\n").title()
    author_name = input("Enter the name of the author for the book:\n").title()
    publication_date = input("Enter the publication date of the book:\n")
    new_book = Book(title, author_name, publication_date, "Available")
    new_book.add_book_to_library()
    for author in authors:
        if author.name == author_name:
            author.add_book(title)

    input(f"You've succesfully added {title} by {author_name} to the library! Press 'enter' to go back.\n ")
    
    return
