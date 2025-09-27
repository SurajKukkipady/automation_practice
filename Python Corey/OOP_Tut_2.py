
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
