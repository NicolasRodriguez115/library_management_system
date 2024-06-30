from app.classes.user import users
def user_details():
    while True:
        select_user = input("Enter the ID of the user to see their information\n")
        for user in users:
            if user.user_id == select_user:
                user.user_details()
                input("Press 'enter' to go back.\n ")
                return
            else:
                try_again = input("That isn't an ID associated to a current user. To try again enter 'yes'. Otherwise enter 'no'\n ").lower()
                if try_again == "yes":
                    input("You'll be able to try again after pressing 'enter'\n ")
                elif try_again == "no":
                    return
                else:
                    input("You didn't enter a valid option. You'll return to the menu after pressing 'enter'.\n ")
                    return