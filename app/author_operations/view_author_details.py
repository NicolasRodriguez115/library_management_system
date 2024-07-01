from app.classes.author import authors
def author_details():
    while True:
        select_author = input("Enter the first and last name of the author you're looking for:\n").title()
        for author in authors:
            if author.name == select_author:
                author.author_details()
                input("Press 'enter' to go back.\n ")
                return
            else:
                try_again = input("That author is not registered in the library yet. To try again enter 'yes'. Otherwise enter 'no'\n ").lower()
                if try_again == "yes":
                    input("You'll be able to try again after pressing 'enter'\n ")
                elif try_again == "no":
                    return
                else:
                    input("You didn't enter a valid option. You'll return to the menu after pressing 'enter'.\n ")
                    return