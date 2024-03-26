import sys

arr = []


def find(num, pl, pr):
    while (pl <= pr):
        x = (pl + pr) // 2

        if sort_array[x] > num:
            pr = x - 1
        elif sort_array[x] < num:
            pl = x + 1
        else:
            return 1

    return 0


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    input = sys.stdin.readline().rstrip().split(" ")
    for i in range(n):
        arr.append(int(input[i]))

    sort_array = sorted(arr)

    finds = int(sys.stdin.readline().rstrip())
    finds_values = sys.stdin.readline().rstrip().split(" ")
    left = 0
    right = n - 1

    for i in range(finds):
        print(find(int(finds_values[i]), left, right))
