from app.classes.user import users
def user_details():
    select_user = input("Enter the ID of the user to see their information\n")
    for user in users:
        print(type(user.user_id))
        print((user.user_id))
        print(select_user == user.user_id)
        input("")
        # if user.user_id == select_user:
        #     user.user_details()
        #     input("Press 'enter' to go back.\n ")
        #     return
        # else:
        #     input("That isn't an ID associated to a current user. You'll return to the main menu after pressing 'enter'\n ")
        #     return