import os
from app.author_operations.add_new_author import new_author
from app.author_operations.view_author_details import author_details
from app.author_operations.display_all_authors import display_authors
def author_operations_menu():
    while True:
        os.system("cls")
        user_input = input("""
Author Operations:                         
    1. Add a new author
    2. View author details
    3. Display all authors
    4. Quit

""")
        if user_input == "1":
            os.system("cls")
            new_author()
        elif user_input == "2":
           os.system("cls")
           author_details()
        elif user_input == "3":
            os.system("cls")
            display_authors()
        elif user_input == "4":
            return
        else:
            input("You've not entered a valid option. Please try again after pressing 'enter'\n ")