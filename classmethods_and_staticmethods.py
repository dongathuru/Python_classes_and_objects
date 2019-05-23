import datetime     # Module for dealing with dates
#
#
#   There are 3 types of methods: Regular, Class and Static methods
#
#
#   Regular: They automatically take in the instance ('self') as 1st
#   argument.
#
class Employee:
    #
    # class variable
    #
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    #
    # classmethods:
    #
    # They automatically take in the class ('cls') as 1st argument.
    # To change a regular method into a class method use a 'decorator'
    # at the beginning: '(@classmethod)'
    #
    @classmethod
    def set_raise_amt(cls, amount):     # Here cls == Employee class.
        cls.raise_amt = amount

    # staticmethods:
    #
    # functions that don't pass in the class or objects automatically,
    # we however use them because they are logically connected to our
    # class.
    # A key indicator is that 'cls' and 'self' are not referenced in
    # their body.
    #
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee('Tom', 'Brady', 100000)
emp2 = Employee('Pam', 'Brady', 120000)
#
# classmethod in action:
#
print(Employee.raise_amt)   # 1.04
Employee.set_raise_amt(1.05)  # Updates the class's raise_amt
print(Employee.raise_amt)   # 1.05
#
# staticmethod in action:
#
#   e.g. to check whether a day is a workday. Python has some special methods
#   that distinguish between weekdays.
#
my_date = datetime.date(2019, 5, 21)
print(Employee.is_workday(my_date)) # True