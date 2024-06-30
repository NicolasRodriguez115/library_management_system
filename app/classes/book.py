library = []

class Book:
    def __init__(self, title, author, publication_date, status):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.status = status

    def add_book_to_library(self):
        library.append(self)

    def show_book(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nPublication Date: {self.publication_date}\nStatus: {self.status}\n---------")
    

    def borrow_book(self):
        if self.status != "Borrowed":
            self.status = "Borrowed"
            return {"Message": "The book was succesfuly borrewed", "Successful" : True}
        else:
            return {"Message": "The book is not available to borrow", "Successful" : False}


    def return_book(self):
        if self.status != "Available":
            self.status = "Available"
            return {"Message": "The book was succesfuly returned", "Successful" : True}
        else:
            return {"Message": "The book is not available to borrow", "Successful" : False}