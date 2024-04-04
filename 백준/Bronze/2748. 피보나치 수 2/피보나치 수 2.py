n = int(input())
d = [0] * (n + 1)


def fibo(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    # 이미 부분 결과값을 계산했다면 해당 결과값을 사용한다
    if d[n] != 0:
        return d[n]

    # 부분 결과값을 계산하지 않았다면 부분 결과값을 계산한다.
    d[n] = fibo(n - 1) + fibo(n - 2)
    return d[n]

print(fibo(n))