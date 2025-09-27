# Why use classes?
# 1. Organize code into logical groups

#A class is a blueprint for creating instances

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

emp1 = Employee()
emp2 = Employee()

print(emp1)
print(emp2)

emp1.first = "Corey"
emp1.last = "Schafer"

emp2.first = "Sue"
emp2.last = "Smith"

print(emp1.first)
print(emp2.last)