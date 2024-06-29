import os
from app.user_operations.add_new_user import new_user
from app.user_operations.view_user_details import user_details
from app.user_operations.display_all_users import display_users
def user_operations_menu():
    os.system("cls")
    while True:
        user_input = input("""
 _   _ _____ ___________   _________________ _____  ___ _____ _____ _____ _   _  _____ 
| | | /  ___|  ___| ___ \ |  _  | ___ \ ___ \  ___|/ _ \_   _|_   _|  _  | \ | |/  ___|
| | | \ `--.| |__ | |_/ / | | | | |_/ / |_/ / |__ / /_\ \| |   | | | | | |  \| |\ `--. 
| | | |`--. \  __||    /  | | | |  __/|    /|  __||  _  || |   | | | | | | . ` | `--. \
| |_| /\__/ / |___| |\ \  \ \_/ / |   | |\ \| |___| | | || |  _| |_\ \_/ / |\  |/\__/ /
 \___/\____/\____/\_| \_|  \___/\_|   \_| \_\____/\_| |_/\_/  \___/ \___/\_| \_/\____/
                           
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