n = int(input())
d = [0] * (n + 2)

d[1] = 1
d[2] = 2


def fibo(n):
    for i in range(3, n + 1):
        d[i] = (d[i - 1] + d[i - 2]) % 15746
    return d[n]

print(fibo(n))