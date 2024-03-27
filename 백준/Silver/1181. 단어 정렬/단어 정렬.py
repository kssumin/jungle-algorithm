import heapq
import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())

    stack = []
    for i in range(n):
        item = sys.stdin.readline().rstrip()
        # 문자열의 길이에 따라 정렬이 되었다
        heapq.heappush(stack, (len(item), item))

    # 중복값을 제거한다
    stack = list(set(stack))

    # 이런식으로 정렬의 기준을 정해줄 수 있음!
    # 첫번째(즉 우리로 따지면 길이를 우선적으로 정렬하고)
    # 두번째 값을 기준으로 정렬하라!
    stack.sort(key=lambda x: (x[0], x[1]))

    for i in range(len(stack)):
        print(stack[i][1])