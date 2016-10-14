# Python Object-Oriented Programming

class Employee:


emp_1 = Employee()
emp_2 = Employee()

# Instance variables that is unique to each isinstance

print(emp_1) 
print(emp_2)


emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay = 5000

emp_2.first = 'Michael'
emp_2.last = 'Ketiku'
emp_2.email = 'mketiku@gmail.com'
emp_2.pay = 5000


print(emp_1.email)
print(emp_2.email)