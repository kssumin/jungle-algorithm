def bfs(node, start_node, arr):
    answer = 0

    queue = []
    visited = [False for _ in range(node + 1)]

    queue.append(start_node)
    visited[start_node] = True

    while queue:
        visited_node = queue.pop(0)

        for neighbor in arr[visited_node]:
            if not visited[neighbor]:
                answer += 1
                queue.append(neighbor)
                visited[neighbor] = True

    return answer


node = int(input())
edge = int(input())
arr = [[] for i in range(node + 1)]

for _ in range(edge):
    x, y = map(int, input().split(" "))
    arr[x].append(y)
    arr[y].append(x)

print(bfs(node, 1, arr))