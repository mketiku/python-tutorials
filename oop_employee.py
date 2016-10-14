# Python Object-Oriented Programming
import datetime

class Employee:
    '''Simple class to hold Employee information at a company'''

    num_of_emps = 0
    raise_amount = 1.04 # class variable
    
    def __init__(self,first,last,pay):
        # init method with attributes of an employee specified
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
         self.pay = int(self.pay * self.raise_amount)# example 
    
    @classmethod
    def set_raise_amt(cls,amount):
        '''
        Regular instance method
        A class method that allows us to set the raise amount
        '''
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        '''
        Alternative constructor
        Construct an employee by parsing a string 
        '''
        first,last, pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def  is_workday(day):
        '''
        Simple function that take a date and returns whether or not
        it was a work day
        '''
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        
emp_1 = Employee('Test','User',9999)
emp_2 = Employee('Michael','Ketiku', 10000)


emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

my_date = datetime.date(2016,10,6)

print(Employee.is_workday(my_date))# Employee.set_raise_amt(1.05)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
