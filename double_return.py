#  Purpose:    Example: a function with two return statements

    if (y == 0):
        print ("division by zero not allowed")
        return
    else:
        print (" returning %f divided by %f " % (x, y))
        return x / y

print (" 5.0 / 2  returns:")
result = division( 5.0 , 2 )
print (result)

print (" 5.0 / 0  returns:")
result = division( 5.0 , 0 )
print (result)