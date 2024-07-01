from app.classes.user import User
import random 
def new_user():
    name = input("Enter the first and last name of the user:\n").title()
    library_id = str(random.randint(100000, 999999))
    new_user = User(name, library_id)
    new_user.new_user()
    input(f"You've succesfully created a user for {name} with customer ID {library_id} to the library! Press 'enter' to go back.\n ")
    return
