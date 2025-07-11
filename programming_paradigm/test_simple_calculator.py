# library_management.py

class Book:
    """
    Represents a single book with a title, author, and checkout status.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """
        Marks the book as checked out if it's available.
        Returns True if successful, False otherwise.
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """
        Marks the book as available if it's checked out.
        Returns True if successful, False otherwise.
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """
        Checks if the book is currently available.
        Returns True if available, False otherwise.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Returns a string representation of the Book object.
        """
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book objects.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """
        Adds a Book object to the library's collection.

        Args:
            book (Book): The Book object to add.
        """
        if isinstance(book, Book):
            self._books.append(book)
            print(f"Added '{book.title}' to the library.")
        else:
            print("Error: Only Book objects can be added to the library.")

    def check_out_book(self, title):
        """
        Finds a book by title and checks it out if available.

        Args:
            title (str): The title of the book to check out.
        """
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out '{title}'.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"'{title}' not found in the library.")

    def return_book(self, title):
        """
        Finds a book by title and returns it if checked out.

        Args:
            title (str): The title of the book to return.
        """
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned '{title}'.")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"'{title}' not found in the library.")

    def list_available_books(self):
        """
        Lists all books that are currently available in the library.
        """
        available_found = False
        for book in self._books:
            if book.is_available():
                print(book)
                available_found = True
        if not available_found:
            print("No books available at the moment.")