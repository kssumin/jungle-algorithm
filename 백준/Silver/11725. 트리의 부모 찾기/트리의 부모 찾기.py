def bfs(start_node):
    queue = []
    queue.append(start_node)
    visited[start_node] = True

    while queue:
        start_node = queue.pop(0)
        neighbor_nodes = arr[start_node]

        for neighbor in neighbor_nodes:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[start_node] = True
                result[neighbor] = start_node


n = int(input())
parent = [i for i in range(n + 1)]
arr = [[] for i in range(n + 1)]
visited = [False for _ in range(n + 1)]

result = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

bfs(1)

for i in range(2, n + 1):
    print(result[i])