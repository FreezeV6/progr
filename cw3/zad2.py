from datetime import date
from typing import List

class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f"Library:\n"
                f"  City: {self.city}\n"
                f"  Street: {self.street}\n"
                f"  Zip Code: {self.zip_code}\n"
                f"  Open Hours: {self.open_hours}\n"
                f"  Phone: {self.phone}")

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"Employee:\n"
                f"  Name: {self.first_name} {self.last_name}\n"
                f"  Hire Date: {self.hire_date}\n"
                f"  Birth Date: {self.birth_date}\n"
                f"  Address: {self.city}, {self.street}, {self.zip_code}\n"
                f"  Phone: {self.phone}")

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

class Order:
    def __init__(self, employee, student, books: List[Book], order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_info = "\n".join(str(book) for book in self.books)
        return (f"Order:\n"
                f"  Employee: {self.employee.first_name} {self.employee.last_name}\n"
                f"  Student: {self.student}\n"
                f"  Order Date: {self.order_date}\n"
                f"  Books:\n{books_info}")

library1 = Library("Warsaw", "Main St 1", "00-001", "8:00 - 18:00", "123456789")
library2 = Library("Krakow", "Market St 5", "30-002", "9:00 - 19:00", "987654321")

employee1 = Employee("Anna", "Kowalska", date(2020, 5, 10), date(1990, 7, 15), "Warsaw", "Main St 2", "00-002", "123123123")
employee2 = Employee("Jan", "Nowak", date(2019, 3, 1), date(1985, 3, 23), "Krakow", "Market St 5", "30-002", "321321321")
employee3 = Employee("Ewa", "Wiśniewska", date(2021, 7, 20), date(1992, 11, 5), "Warsaw", "Main St 3", "00-003", "456456456")

books = [
    Book(library1, date(2000, 5, 15), "Henryk", "Sienkiewicz", 300),
    Book(library2, date(2010, 8, 10), "Adam", "Mickiewicz", 250),
    Book(library1, date(2018, 2, 3), "Maria", "Konopnicka", 400),
    Book(library1, date(2022, 6, 5), "Juliusz", "Słowacki", 150),
    Book(library2, date(1995, 10, 25), "Stefan", "Żeromski", 220)
]

students = ["Piotr Majewski", "Agnieszka Zielinska", "Tomasz Kowalczyk"]

order1 = Order(employee1, students[0], [books[0], books[2]], date(2023, 5, 20))
order2 = Order(employee2, students[1], [books[1], books[3], books[4]], date(2023, 6, 15))

print(order1)
print(order2)
