# Python Object-Oriented Programming

class Employee:
    '''Simple class to hold Employee information at a company'''

    
    def __init__(self,first,last,pay):
        # init method with attributes of an employee specified
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
emp_1 = Employee('Test','User',9999)
emp_2 = Employee('Michael','Ketiku', 10000)

# Instance variables that is unique to each isinstance

print(emp_1.email)
print(emp_2.email)

# print(emp_1.fullname()) # parantheses allows us to use the actual method instead of the name.
# print(emp_2.fullname())

print(emp_1.fullname()) # instance employee 1 
print(Employee.fullname(emp_1))