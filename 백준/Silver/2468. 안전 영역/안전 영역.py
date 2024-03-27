import sys

sys.setrecursionlimit(10**6)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, h):
    for m in range(4):
        nx = x + dx[m]
        ny = y + dy[m]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] > h:
            visited[nx][ny] = True
            dfs(nx, ny, h)


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())

    # 초기화
    visited = [[False for j in range(n)] for i in range(n)]
    arr = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        values = sys.stdin.readline().rstrip().split(" ")
        for j in range(n):
            arr[i][j] = int(values[j])

    answer = 0
    for h in range(0, max(map(max, arr)) + 1):
        temp = 0
        visited = [[False for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if arr[i][j] > h and not visited[i][j]:
                    temp += 1
                    dfs(i, j, h)

        if temp > answer:
            answer = temp

    print(answer)