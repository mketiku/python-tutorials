def fizzbuzz():
    for num in range(1, 101):
        if num % 5 == 0 and num % 3 == 0:
            print ("FizzBuzz")
        elif num % 3 == 0:
            print ("Fizz")
        elif num % 5 == 0:
            print ("Buzz")
        else:
            print (num)

    return
# fizzbuzz()

# def fib_1():
#     a,b = 0,1
#     for i in range(0, 10):
#         print (a)
#         a,b = b, a + b
#     return 1

# def fib(n):
    '''
    Running time O(2^n)
    '''
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)


# print(fib(30))

# def rec_fib(n):
#     '''inefficient recursive function as defined, returns Fibonacci number'''
#     if n > 1:
#         return rec_fib(n-1) + rec_fib(n-2)
#     return n

# for i in range(40):
#     print (i, rec_fib(i))


def fibonacci(x):

    List = []
    f = 1
    List.append(f)
    List.append(f)  # because the fibonacci sequence has two 1's at first
    while f <= x:
        # says that f = the sum of the last two f's in the series
        f = List[-1] + List[-2]
        List.append(f)
    else:
        # because the code lists the fibonacci number one past x. Not
        # necessary, but defines the code better
        List.remove(List[-1])
        for i in range(0, len(List)):
            # prints it in series form instead of list form. Also not necessary
            print (List[i])


fibonacci(10001)