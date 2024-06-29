from app.classes.book import Book

def new_book():
    title = input("Enter the title of the book:\n").title()
    author = input("Enter the name of the author for the book:\n").title()
    publication_date = input("Enter the publication date of the book:\n")
    new_book = Book(title, author, publication_date, "Available")
    new_book.add_book_to_library()
    # books.append(Book(title, author, publication_date, "Available"))
    input(f"You've succesfully added {title} by {author} to the library! Press 'enter' to go back.\n ")
    return