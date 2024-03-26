import sys


def find(sorted_arr, m, left, right):
    while (left <= right):
        sum = 0
        mid = (left + right) // 2

        for i in range(n):
            if int(sorted_arr[i]) - mid > 0:
                sum += int(sorted_arr[i])-mid

        # 나무의 합계가 원하는 합계와 같거나 더 클 때는 더 많이 자른다.
        if sum >= m:
            left = mid + 1

        # 나무의 합계가 원하는 합계보다 더 적을 때는 더 적게 자른다.
        else:
            right = mid - 1

    return right


if __name__ == '__main__':
    input = sys.stdin.readline().rstrip().split(" ")
    n = int(input[0])
    m = int(input[1])
    arr = []

    arr_input = sys.stdin.readline().rstrip().split(" ")
    for i in range(n):
        arr.append(arr_input[i])

    left = 0
    right = 1000000000

    print(find(arr, m, left, right))
