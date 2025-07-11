class Book:
    """
    A class to represent a book with title, author, and publication year.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Initializes a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Prints a message upon object deletion."""
        print(f"Deleting {self.title}")

    def __str__(self) -> str:
        """Returns a user-friendly string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """Returns an official string representation to recreate the instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"