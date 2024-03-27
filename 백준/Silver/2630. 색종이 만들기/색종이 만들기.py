import sys


def find(x1, x2, y1, y2):
    global sum_white, sum_blue

    # 종료조건(가리키는 인덱스가 같을 때 즉 하나일 떄)
    if x1 == x2 and y1 == y2:
        if arr[x1][y1] == 0:
            sum_white += 1
        else:
            sum_blue += 1

    else:
        # 모두 화이트라고 한다면
        if isAllWhite(x1, x2, y1, y2):
            sum_white += 1
        # 모두 파란색이라고 한다면
        elif isAllBlue(x1, x2, y1, y2):
            sum_blue += 1
        # 색깔이 섞여있다면
        else:
            find(x1, (x2 + x1) // 2, y1, (y2 + y1) // 2)
            find((x2 + x1) // 2 + 1, x2, y1, (y2 + y1) // 2)
            find(x1, (x2 + x1) // 2, (y2 + y1) // 2 + 1, y2)
            find((x2 + x1) // 2 + 1, x2, (y2 + y1) // 2 + 1, y2)

# 주어긴 길이는 모두 화이트 인지 확안
def isAllWhite(x1, x2, y1, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if arr[i][j] == 1:
                return False

    return True


# 주어긴 길이는 모두 파란색 인지 확인
def isAllBlue(x1, x2, y1, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if arr[i][j] == 0:
                return False

    return True


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())

    # 배열 초기화
    arr = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        input_arr = sys.stdin.readline().rstrip().split(" ")
        for j in range(n):
            arr[i][j] = int(input_arr[j])

    sum_white = 0
    sum_blue = 0

    # 길이가 아니라 인덱스 기준
    find(0, n - 1, 0, n - 1)

    print(sum_white)
    print(sum_blue)