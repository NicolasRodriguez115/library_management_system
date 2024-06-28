import os
from add_new_book import new_book
from borrow_book import borrow_book
from return_book import book_return
from search_for_book import search_book
from display_books import books_display
def book_operations_menu():
    os.system("cls")
    while True:
        user_input = input("""
Book Operations:
    1. Add a new book
    2. Borrow a book
    3. Return a book
    4. Search for a book
    5. Display all books
    6. Quit
                           
""")
        if user_input == "1":
            new_book()
        elif user_input == "2":
            borrow_book()
        elif user_input == "3":
            book_return()
        elif user_input == "4":
            search_book()
        elif user_input == "5":
            books_display()
        elif user_input == "6":
            return
        else:
            input("You've not entered a valid option. Please try again after pressing 'enter'\n ")