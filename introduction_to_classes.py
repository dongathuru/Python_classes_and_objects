# Classes and Objects:
#
#
# Python is primarily designed as an object­oriented programming
# language.
#
# You can think of a class as a sort of template; a guide for the way
# an object should be structured.
# Each object belongs to a class and inherits the properties of that
# class, but acts individually to the other objects of that class.
#
# An object is sometimes referred to as an ‘instance’ of a class and
# Classes can be thought of as blueprints for creating objects.
#
#
# The simplest class you should define is a simple subclass of the base
# object that does nothing.
#
class NoOp(object):
    pass
#
class Employee:
    # The __init__ method is an important one to do all your setup steps.
    # The instance is passed first 'self'.
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    # The instance is passed first 'self'.
    def fullname(self):
        return '{} {}' .format(self.first, self.last)

#
# Creating objects of the class
#
emp1 = Employee('Pat', 'Rodgers', 65000)
emp2 = Employee('Joy', 'Rodgers', 50000)

#
#   Notice the end empty brackets for calling methods
#
print(emp1.fullname())  # Pat Rodgers
