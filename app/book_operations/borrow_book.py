from app.classes.book import library

def borrow_book():
    title = input("Enter the name of the book:\n").title()
    author = input("Enter the name of the author:\n").title()
    for book in library:
        if book.title == title and book.author == author:
            response = book.borrow_book()
            input(f"{response["Message"]} Press 'enter' to go back")
    
    return