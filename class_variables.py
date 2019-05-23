#   Instance variables are set with the 'self' and '__init__' method
#   Class variables are shared amongst all instances

class Employee:

    raise_amount = 1.04     # That's how 4% is represented
    no_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        # We can do functionality in the __init__ with no 'self' as below:
        Employee.no_of_emps += 1 # Increments with each instance creation

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # Notice the int(...)

print(Employee.no_of_emps) # 0
emp1 = Employee('Pat', 'Rodgers', 50000)
emp2 = Employee('Jane', 'Rodgers', 60000)
print(Employee.no_of_emps) # 2

print()

print(emp1.pay) # 50000
emp1.apply_raise()
print(emp1.pay) # 52000

print()

print(emp2.pay) # 60000
Employee.raise_amount = 2 # Can be accessed & updated outside
emp2.apply_raise()
print(emp2.pay) # 120000