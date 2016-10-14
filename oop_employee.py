# Python Object-Oriented Programming
import datetime


class Employee:
    '''Simple class to hold Employee information at a company'''

    num_of_emps = 0
    raise_amount = 1.04  # class variable

    def __init__(self, first, last, pay):
        # init method with attributes of an employee specified
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # example

    @classmethod
    def set_raise_amt(cls, amount):
        '''
        Regular instance method
        A class method that allows us to set the raise amount
        '''
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        '''
        Alternative constructor
        Construct an employee by parsing a string 
        '''
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        '''
        Simple function that take a date and returns whether or not
        it was a work day
        '''
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    '''
    Inherits all the attributes and methods from the Employee class
    '''
    raise_amt = 1.10
    # Overrides the raise amoutn for a given Employee

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # pass first, last, pay from the employee so we don't repeat ourselves'
        self.prog_lang = prog_lang


class Manager(Employee):
    '''
    Inherits all the attributes and methods of the Employee class
    '''

    def __init__(self, first, last, pay, employees=None):
        '''
        Add a list of employees that a manager supervises to attributes list
        Allow the list of employees to be empty, if it is not proceed 
        '''
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


dev_1 = Developer('Test', 'User', 9999, 'Python')
dev_2 = Developer('Michael', 'Ketiku', 10000, 'Java')

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'


# Allows a user to view the method resolution order for a class
# print(help(Developer))
# print(dev_1.email)


# print(dev_2.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_2.email)
# print(dev_2.prog_lang)

mgr_1 = Manager('Sue', 'Sue', 10000, [dev_1])

# mgr_1.add_emp(dev_2) # easily add and remove employees from an employee
# mgr_1.remove_emp(dev_1)

# print(mgr_1.email)
# mgr_1.print_emp()

# print(isinstance(Manager, Manager))

