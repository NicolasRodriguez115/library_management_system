from app.classes.book import library
def books_display():
    print("""
  ____   ___   ___  _  ______  
 | __ ) / _ \ / _ \| |/ / ___| 
 |  _ \| | | | | | | ' /\___ \ 
 | |_) | |_| | |_| | . \ ___) |
 |____/ \___/ \___/|_|\_\____/
---------
          """)
    for book in library:
        book.show_book()
    input("When you're done checking the list of books press 'enter'.\n ")
    return