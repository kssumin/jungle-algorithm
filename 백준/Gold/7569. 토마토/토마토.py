import sys
from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]
answer = 0


def bfs():
    while queue:
        result = check()
        if result != -1:
            return result

        current_h, current_x, current_y = queue.popleft()

        for i in range(6):
            next_x, next_y, next_h = current_x + dx[i], current_y + dy[i], current_h + dh[i]

            if not_range(next_x, next_y, next_h):
                continue

            if cannot_go(next_x, next_y, next_h):
                continue

            graph[next_h][next_x][next_y] = graph[current_h][current_x][current_y] + 1
            visited[next_h][next_x][next_y] = True
            queue.append((next_h, next_x, next_y))


def not_range(current_x, current_y, current_h):
    if current_x < 0 or current_x >= n or current_y < 0 or current_y >= m or current_h < 0 or current_h >= h:
        return True

    if visited[current_h][current_x][current_y]:
        return True

    return False


def cannot_go(current_x, current_y, current_h):
    if graph[current_h][current_x][current_y] == -1:
        return True
    return False


def check():
    global answer
    for a in range(h):
        for b in range(n):
            for c in range(m):
                if graph[a][b][c] == 0:
                    return -1
                if graph[a][b][c] > answer:
                    answer = graph[a][b][c]

    return answer - 1


m, n, h = map(int, input().split(" "))
graph = [[list(map(int, input().split(" "))) for _ in range(n)] for _ in range(h)]
visited = [[[False] * m for _ in range(n)] for _ in range(h)]
queue = deque()

# 1인 경우(토마토가 익은 경우)를 모두 찾아서 우선 큐에 넣는다.
for a in range(h):
    for b in range(n):
        for c in range(m):
            if graph[a][b][c] == 1 and visited[a][b][c] == False:
                queue.append((a, b, c))
                visited[a][b][c] = True

# 시작 지점을 모두 찾은 후에 시자한다
bfs()

print(check())