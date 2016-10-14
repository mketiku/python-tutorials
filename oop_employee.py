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
    
    def __repr__(self):
        '''
        Representation of an employee that allows a developer to recreate the object
        '''
        return "Employee('{}', '{}', '{}')".format(self.first,self.last,self.pay)
    
    def __str__(self):
        '''
        String representation of an employtee that is displayed to an enduser
        '''
        return '{} - {}'.format(self.fullname(),self.email)

    def __add__(self,other):
        '''
        Return an employee added together
        '''
        return self.pay + other.pay

    def __len__(self):
        '''
        Return the length of an employees full name, not useful
        in the real world, but it is helpful to understand special methods
        '''
        return len(self.fullname())

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
        # Init is a special __dunder__ method
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



emp_1 = Employee('Test', 'User', 9999)
emp_2 = Employee('Michael', 'Ketiku', 10000)


print(len(emp_1))
# print(str(emp_1)) # end user represenation
# print(emp_1)


# print(1+2)
# print(int.__add__(1,2))
# print(str.__add__('1','2')) # This determines what a addition function displays as

# # repr(emp_1)
# # str(emp_1)

# print(emp_1+emp_2) # using a special dunder method to add 2 employees pay together

