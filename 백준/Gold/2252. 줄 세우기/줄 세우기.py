import sys

sys.setrecursionlimit(999999)

def dfs(node):
    visited[node] = True
    for next_vertex in arr[node]:
        in_edge[next_vertex] -= 1

        if in_edge[next_vertex] == 0:
            answer.append(next_vertex)
            dfs(next_vertex)


n, m = map(int, input().split(" "))
arr = [[] for _ in range(n + 1)]
in_edge = [0 for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
answer = []

for i in range(m):
    x, y = map(int, input().split(" "))
    arr[x].append(y)
    in_edge[y] += 1

# 진입차수가 0인 간선을 모두 넣는다
for node in range(1, n + 1):
    if in_edge[node] == 0 and visited[node]==False:
        answer.append(node)
        dfs(node)

print(*answer)