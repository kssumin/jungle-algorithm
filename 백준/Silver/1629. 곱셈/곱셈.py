import sys


def get(a, b, c):
    if b == 1:
        return a % c
    # 2로 나누어지지 않는다면
    if b % 2 == 0:
        return (get(a, b // 2, c) ** 2) % c
    # 2로 나누어 떨어진다면
    else:
        return ((get(a, b // 2, c) ** 2) * a) % c


if __name__ == "__main__":
    input_num = sys.stdin.readline().rstrip().split(" ")

    a = int(input_num[0])
    b = int(input_num[1])
    c = int(input_num[2])

    print(get(a, b, c))
