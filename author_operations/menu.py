import os
from add_new_author import new_author
from view_author_details import author_details
from display_all_authors import display_authors
def author_operations_menu():
    os.system("cls")
    while True:
        user_input = input("""
Author Operations:
    1. Add a new author
    2. View author details
    3. Display all authors
    4. Quit
                           
""")
        if user_input == "1":
            new_author()
        elif user_input == "2":
           author_details()
        elif user_input == "3":
            display_authors()
        elif user_input == "4":
            return
        else:
            input("You've not entered a valid option. Please try again after pressing 'enter'\n ")