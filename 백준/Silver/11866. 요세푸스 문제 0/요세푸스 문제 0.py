import sys
from collections import deque

# 파이썬에서는 리스트 회전을 deque 콜렉션을 통해 제공한다
# queue.rotate(양수) : 오른쪽 회전
# queue.rotate(음수) : 왼쪽 회전
if __name__ == "__main__":
    input_value = sys.stdin.readline().rstrip().split(" ")

    n = int(input_value[0])
    k = int(input_value[1])

    circular_queue = deque([i for i in range(1, n + 1)])
    answer = []

    for _ in range(n):
        circular_queue.rotate(-k + 1)
        answer.append(circular_queue.popleft())

    formatted_str = "<" + ", ".join(map(str, answer)) + ">"
    print(formatted_str)