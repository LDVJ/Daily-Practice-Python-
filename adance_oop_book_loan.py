class BookNotAvailableError(Exception):
    def __init__(self, message : str, title : str):
        super().__init__(message)
        self.book_title = title

class InvalidReturnError(Exception):
    def __init__(self, message : str, title : str):
        super().__init__(message)
        self.book_title = title


class Book:
    # constructor function with all attributes as private
    def __init__(self, title :str, total_copies : int):
        self.__book_title = title
        self.__available_books = self.__total_copies = total_copies

    # gettter function for the title
    def get_title(self):
        return self.__book_title
    
    # getter function for the available books
    def get_available_books(self):
        return self.__available_books
    
    # getter function for the available books
    def get_total_copies(self):
        return self.__total_copies
    
    def set_total_copies(self, n : int):
        if n > 0:
            self.__total_copies = n
        else:
            print("Invalid: copies must be greater than 0")

    def borrow(self):
        if self.__available_books > 0:
            self.__available_books -= 1
            print(f"Thank you. For borrowing book {self.__book_title}")
        else:
            raise BookNotAvailableError(f"Requested book is not avilable at the moment", self.__book_title)

    
    def return_book(self):
        if self.__available_books < self.__total_copies:
            self.__available_books += 1
            print("Book Returned Successfully")
        else:
            raise InvalidReturnError(f"All Books are already returned", self.__book_title)


book1 = Book("Clean Code",2)
try:
    book1.borrow()
    book1.borrow()
    book1.borrow()
except BookNotAvailableError as e:
    print("Error",e)

try:
    book1.return_book()
    book1.return_book()
    book1.return_book()
except InvalidReturnError as e:
    print("Error",e)
