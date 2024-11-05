class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"Book:\n"
                f"  Author: {self.author_name} {self.author_surname}\n"
                f"  Publication Date: {self.publication_date}\n"
                f"  Pages: {self.number_of_pages}\n"
                f"  {self.library}")
