'''
write function right_justify that takes a stringnamed s as a parameter and prints it with enough leading spaces so that the last letter of the string is in the column 70 of the display.
'''


def right_justify(s):
    x = len(str(s))
    if x <= 70:
        y = 70 - x
        print (' ' * y + s) 
    else:
        print ("string length exceeds column width")

right_justify()

def print_spam():
    print('spam')
def do_twice(f):
    f()
    f()
do_twice(print_spam)

do_twice(print_twice, "spam")



def do_twice(print_twice, arg):
    '''
    function do_twice takes 2 arguments(function object print_twice and a generic argument)
    then it calls the function print_twice and passes the argument to it

    '''
    print_twice(arg)
    print_twice(arg)

def print_twice(arg):
    print(arg)
    print(arg)

def do_four(print_twice, arg):
    '''
    function do_four takes 2 arguments and returns a nested function twice
    '''
     do_twice(print_twice, arg)
     do_twice(print_twice, arg)



