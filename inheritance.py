#   Inheritance allows us to add functionality without affecting the
#   parent e.g. below types of Employees
class Employee:

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}' .format(self.first, self.last)

    def apply_raise(self):
        self.pay = self.pay * self.raise_amt

class Developer(Employee):

    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)      # 1st 3 are handle by parent's __init__
        self.prog_lang = prog_lang              # Handled by current __init__


help(Developer) #   Allows us to clearly see the mro (Method Resolution Order)
#   And also see the chain of inheritance.

#   Below is to show that the Developer --> Employee inheritance works.
dev1 = Developer('Pat', 'Smith', 150000, 'Python')
dev2 = Developer('Jen', 'Smith', 110000, 'Java')
print(dev1.email)
print(dev2.prog_lang)

#   Suppose we want to create a manager class so that we can set how many
#   people a manager manages:
class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())

mg1 = Manager('John', 'Smith', 300000, [dev1])
print(mg1.email)
mg1.add_emp(dev2)
mg1.remove_emp(dev1)
mg1.print_emp()

print(isinstance(dev1, Developer))
print(issubclass(Developer, Employee))
