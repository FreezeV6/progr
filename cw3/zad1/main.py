from cw3.zad1.Student.Student import Student

student1 = Student("Alice", [60, 70, 80])
student2 = Student("Bob", [30, 40, 20])

(student1.name, student1.is_passed()), (student2.name, student2.is_passed())

print(student1.name, student1.is_passed())
print(student2.name, student2.is_passed())
