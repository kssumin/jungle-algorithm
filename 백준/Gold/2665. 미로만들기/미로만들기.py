import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(node_x, node_y, answer):
    queue = []
    heapq.heappush(queue, (answer, node_x, node_y))
    visited[node_x][node_y] = True

    while queue:
        answer, node_x, node_y = heapq.heappop(queue)

        for i in range(4):
            next_x, next_y = node_x + dx[i], node_y + dy[i]

            # 도착지점
            if is_end(next_x, next_y):
                return answer

            if not_range(next_x, next_y):
                continue

            if validate_already_go(next_x, next_y):
                continue

            if can_not_go(next_x, next_y):
                visited[next_x][next_y] = True
                heapq.heappush(queue, (answer + 1, next_x, next_y))
            else:
                # 검은색이 아닐 경우 새롭게 바꾸지 않아도 된다.
                visited[next_x][next_y] = True
                heapq.heappush(queue, (answer, next_x, next_y))


def not_range(next_x, next_y):
    if next_x <= 0 or next_x >= n + 1 or next_y <= 0 or next_y >= n + 1:
        return True
    return False


def is_end(next_x, next_y):
    if next_x == n and next_y == n:
        return True
    return False


def can_not_go(next_x, next_y):
    # 검은색은 가지 못 한다
    if arr[next_x][next_y] == 0:
        return True
    return False


def validate_already_go(next_x, next_y):
    return visited[next_x][next_y]


n = int(input())
arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
visited = [[False for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    values = input()
    for j in range(1, n + 1):
        arr[i][j] = int(values[j - 1])

print(bfs(1, 1, 0))