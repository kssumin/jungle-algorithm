import sys


def get(index, item):
    while stack:
        # 현 값이 더 크다
        if stack[-1][1] < item:
            stack.pop()
        # 현 값이 더 작거나 같다
        else:
            temp = stack[-1][0]
            stack.append((index, item))
            return temp

    stack.append((index, item))
    return 0


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    input_value = sys.stdin.readline().rstrip().split(" ")
    answer = []
    stack = []

    for i in range(len(input_value)):
        answer.append(get(i + 1, int(input_value[i])))

    result_string = ' '.join(map(str, answer))
    print(result_string)