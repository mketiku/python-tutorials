# Complete the function below.


def StairCase(N):
    '''Print out a staircase. '''
    for i in range(1,N+1):
        # print()
        hashes = "#" * i
        spaces = " " * (N-i)
        result = spaces + hashes
        print(result)

N = int(input())
StairCase(N)
