from app.classes.book import library
from app.classes.user import users
def return_book():
        while True:
            title = input("Enter the name of the book:\n").title()
            author = input("Enter the name of the author:\n").title()
            user_id = input(
        """ Enter the ID of the user who borrowed the book 
        (if the user doesn't have a user ID just press 'enter'):\n """)
            for book in library:
                if book.title == title and book.author == author:
                    response = book.return_book()
                    print(response["Message"])
                    for user in users:
                        if user.user_id == user_id:
                            user.book_returned(book.title)
                            return
                        else:
                            # qué puedo hacer para el caso en el que ingresen un id pero lo pongan mal
                            return
                else:
                    try_or_exit = input(
        """That information doesn't match any book in the library 
        (make sure that you spelled the title and name of the author correctly). 
        If you want to try again enter 'yes'. If you want to go exit enter 'no'.\n""").lower()
                    if try_or_exit == "yes":
                        input("You'll be able to try again after pressing 'enter'\n ")
                    elif try_or_exit == "no":
                        return
                    else:
                        input("You didn't enter a valid option. You'll return to the menu after pressing 'enter'.\n ")
                        return