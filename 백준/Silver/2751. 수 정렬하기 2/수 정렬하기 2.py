import sys
import heapq

if __name__ == "__main__":
    arr = []
    value = int(sys.stdin.readline().rstrip())

    for _ in range(value):
        n = int(sys.stdin.readline().rstrip())
        heapq.heappush(arr, n)

    for _ in range(len(arr)):
        print(heapq.heappop(arr))