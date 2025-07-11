class Book:
    """A base class for a book with a title and author."""
    def __init__(self, title: str, author: str):
        """Initializes the book's title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Returns a string representation for a generic book."""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """A derived class for an electronic book, inheriting from Book."""
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initializes the EBook, calling the base class constructor
        and setting the file size.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Returns a string representation for an EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """A derived class for a physical book, inheriting from Book."""
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initializes the PrintBook, calling the base class constructor
        and setting the page count.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Returns a string representation for a PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """A class to manage a collection of various book types."""
    def __init__(self):
        """Initializes the library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Adds a book instance to the library's collection."""
        self.books.append(book)

    def list_books(self):
        """Prints the details of each book in the library."""
        for book in self.books:
            print(book)