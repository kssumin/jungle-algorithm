"""
시간초과


"""


def bfs(start_node):
    queue = []
    visited = [False] * (n + 1)

    visited[start_node] = True
    queue.append([start_node, 0])

    while queue:
        node = queue.pop(0)

        node_value = node[0]
        node_dis = node[1]

        if node_dis == k:
            answer.add(node_value)

        if node_dis > k:
            continue

        for neighbor_node in arr[node_value]:
            if not visited[neighbor_node]:
                temp = node_dis + 1

                visited[neighbor_node] = True
                queue.append([neighbor_node, temp])


n, m, k, x = map(int, input().split())
answer = set()

arr = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split(" "))
    arr[a].append(b)

bfs(x)

if not answer:
    print(-1)
else:
    answer = sorted(answer)
    for each in answer:
        print(each)