def prime_sieve(n):
    b = []
    p = 2
    b.append(0)
    a = b[:]
    # a[0] == 0 #potential issue
    print(a)
    for i in range(1,n):
        a[i] = 1
    while (p**2) <= n:
        j = p ** 2
        while j <= n:
            a[j] = 0
            j += p
        p += 1
        if (a[p] == 1):
            break
    return(a)

prime_sieve(4)