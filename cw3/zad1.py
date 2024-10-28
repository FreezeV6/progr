class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50

student1 = Student("Alice", [60, 70, 80])
student2 = Student("Bob", [30, 40, 20])

(student1.name, student1.is_passed()), (student2.name, student2.is_passed())

print(student1.name, student1.is_passed())
print(student2.name, student2.is_passed())
