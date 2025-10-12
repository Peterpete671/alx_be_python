class Book:
    def __init__(self, title, author, year):
        """Initializes a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """String representation for readable output."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation used for debugging and recreation."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Prints a message when the object is deleted."""
        print(f"Deleting {self.title}")
