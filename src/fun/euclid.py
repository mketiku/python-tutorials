def gcd(x, y):
    '''Compute the Greatest common denomininator of a x and y integers '''
    while y != 0:
        (x, y) = (y, x % y)
    return x


res = gcd(20,100000)
print(res)