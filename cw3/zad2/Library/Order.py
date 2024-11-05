from typing import List
from cw3 import Book


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
