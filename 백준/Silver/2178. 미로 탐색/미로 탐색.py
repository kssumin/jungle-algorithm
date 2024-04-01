dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j, arr):
    queue = []
    visited = [[False for _ in range(m + 1)] for _ in range(n + 1)]

    queue.append([i, j])
    visited[i][j] = True
    arr[i][j] = 1

    while queue:
        node = queue.pop(0)
        current_x = node[0]
        current_y = node[1]

        # 목표에 도달하지 못 했다면 다음 노드로 이동한다
        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            # 범위 안이 아니라면
            if not validate_range(next_x, next_y):
                continue

            # 방문을 이미 했다면
            if visited[next_x][next_y]:
                continue

            # 지나갈 수 없는 지점이라면
            if arr[next_x][next_y] == 0:
                continue

            # 범위 안이고 방문을 안 했다면
            queue.append([next_x, next_y])
            visited[next_x][next_y] = True
            arr[next_x][next_y] = arr[current_x][current_y] + 1


def validate_range(i, j):
    if i <= 0 or i > n or j <= 0 or j > m:
        return False
    return True


def is_end(i, j):
    if i == n and j == m:
        return True
    return False


n, m = map(int, input().split())
arr = [[0 for i in range(m + 1)] for j in range(n + 1)]

for i in range(1, n + 1):
    temp = list(input())
    for j in range(1, m + 1):
        arr[i][j] = int(temp[j - 1])

bfs(1, 1, arr)
print(arr[n][m])