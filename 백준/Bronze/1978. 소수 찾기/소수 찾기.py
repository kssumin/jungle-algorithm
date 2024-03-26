import math
import sys


# 소수인지 검사한다.
def isPrime(n):
    # 1보다 작거나 같으면 소수가 아니다
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        # 나누어 떨어지면 소수가 아니다
        if n % i == 0:
            return False
    # 모든 수로 나누어 떨어지지 않으므로 소수이다.
    return True


if __name__ == '__main__':
    reply = int(sys.stdin.readline().rstrip())
    count = 0

    arr = sys.stdin.readline().rstrip().split(" ")

    for num in range(reply):
        # 소수인면 수를 업데이트한다.
        if isPrime(int(arr[num])):
            count += 1

    print(count)
