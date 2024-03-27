import sys


class CircularQueue:
    def __init__(self, n):
        self.front = -1
        self.rear = -1
        self.n = n
        self.items = [None] * (n + 1)
        self.total = n + 1

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return (self.rear + 1) % (self.total) == self.front

    def clear(self):
        self.front = self.rear

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.total
            self.items[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.total
            item = self.items[self.front]
            self.items[self.front] = None
            return item

    def peek(self):
        if not self.isEmpty():
            return self.items[self.front]


def find(n, k):
    queue = CircularQueue(n)
    answer = []

    for i in range(1, n + 1):
        queue.enqueue(i)

    """
    큐가 비면 값을 빼는 것을 중단한다.
    """
    while not queue.isEmpty():
        count = 0
        for _ in range(k - 1):
            if not queue.isEmpty():
                count += 1
                # 큐가 비어 있는지 먼저 확인
                item = queue.dequeue()
                queue.enqueue(item)

        # 큐가 비어 있지 않은 경우에만 값을 추가
        answer.append(queue.dequeue())
    return answer


if __name__ == "__main__":
    input_value = sys.stdin.readline().rstrip().split(" ")

    n = int(input_value[0])
    k = int(input_value[1])

    answer = find(n, k)
    formatted_str = "<" + ", ".join(map(str, answer)) + ">"
    print(formatted_str)