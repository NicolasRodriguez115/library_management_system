import os
from add_new_user import new_user
from view_user_details import user_details
from display_all_users import display_users
def user_operations_menu():
    os.system("cls")
    while True:
        user_input = input("""
User Operations:
    1. Add a new user
    2. View user details
    3. Display all users
    4. Quit
                           
""")
        if user_input == "1":
            new_user()
        elif user_input == "2":
           user_details()
        elif user_input == "3":
            display_users()
        elif user_input == "4":
            return
        else:
            input("You've not entered a valid option. Please try again after pressing 'enter'\n ")