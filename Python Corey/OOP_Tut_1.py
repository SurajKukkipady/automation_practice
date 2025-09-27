# Why use classes?
# 1. Organize code into logical groups

#A class is a blueprint for creating instances

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

emp1 = Employee('John', 'Doe', 50000)
emp2 = Employee('Jane', 'Smith', 60000)

# print(emp1)
# print(emp2)

print(emp1.first)
print(emp2.last)

print(emp1.fullname())
print(emp2.fullname())