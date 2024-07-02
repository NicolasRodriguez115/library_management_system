from app.classes.user import users
def user_details():
    select_user = input("Enter the ID of the user to see their information\n")
    
    for user in users:
        if user.user_id == select_user:
            user.user_details()
            input("Press 'enter' to go back.\n ")
            return
        
    input("That isn't an ID associated to a current user. You'll return to the main menu after pressing 'enter'\n ")
    return