import os
from app.author_operations.add_new_author import new_author
from app.author_operations.view_author_details import author_details
from app.author_operations.display_all_authors import display_authors
def author_operations_menu():
    while True:
        os.system("cls")
        user_input = input("""
  ___  _   _ _____ _   _ ___________   _________________ _____  ___ _____ _____ _____ _   _  _____ 
 / _ \| | | |_   _| | | |  _  | ___ \ |  _  | ___ \ ___ \  ___|/ _ \_   _|_   _|  _  | \ | |/  ___|
/ /_\ \ | | | | | | |_| | | | | |_/ / | | | | |_/ / |_/ / |__ / /_\ \| |   | | | | | |  \| |\ `--. 
|  _  | | | | | | |  _  | | | |    /  | | | |  __/|    /|  __||  _  || |   | | | | | | . ` | `--. \
| | | | |_| | | | | | | \ \_/ / |\ \  \ \_/ / |   | |\ \| |___| | | || |  _| |_\ \_/ / |\  |/\__/ /
\_| |_/\___/  \_/ \_| |_/\___/\_| \_|  \___/\_|   \_| \_\____/\_| |_/\_/  \___/ \___/\_| \_/\____/
                           
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