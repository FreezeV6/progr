from datetime import date

from cw3.zad2.Library.Book import Book
from cw3.zad2.Library.Employee import Employee
from cw3.zad2.Library.Library import Library
from cw3.zad2.Library.Order import Order

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
