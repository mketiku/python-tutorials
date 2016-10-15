import sys

table = [0]*1000

def FastFib(n):
    if n<=1:
        return n
    else:
        if(table[n-1]==0):
            table[n-1] = FastFib(n-1)
        if(table[n-2]==0):
            table[n-2] = FastFib(n-2)
        table[n] = table[n-1] + table[n-2]
        return table[n]

def main():
    print('Enter a number : ')
    num = int(sys.stdin.readline())
    print(FastFib(num))

if __name__=='__main__':
    main()