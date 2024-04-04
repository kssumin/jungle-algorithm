from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    mid_answer = 0
    while queue:
        current_x, current_y = queue.pop()
        mid_answer += 1

        for i in range(4):
            next_x, next_y = current_x + dx[i], current_y + dy[i]

            if cannot_go(next_x, next_y):
                continue

            visited[next_x][next_y] = True
            queue.append((next_x, next_y))

    result.append(mid_answer)


def cannot_go(i, j):
    if i < 0 or i >= n or j < 0 or j >= n:
        return True
    if visited[i][j]:
        return True

    if arr[i][j] == 0:
        return True

    return False


n = int(input())
arr = [[0 for i in range(n)] for j in range(n)]
visited = [[False for i in range(n)] for j in range(n)]
result = []
queue = deque()

for i in range(n):
    values = input()
    for j in range(n):
        arr[i][j] = int(values[j])

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visited[i][j] == False:
            visited[i][j] = True
            queue.append((i, j))
            bfs()

answer = sorted(result)

print(len(answer))
for a in answer:
    print(a)