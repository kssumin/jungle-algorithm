import sys

def input():
    return sys.stdin.readline().rstrip()

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == '__main__':
    n = int(input())
    print(factorial(n))