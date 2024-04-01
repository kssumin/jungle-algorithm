def find(node):
    if parent[node] == node:
        return parent[node]
    else:
        return find(parent[node])


def union(node1, node2):
    a = find(node1)
    b = find(node2)

    # 부모 자체를 바궈야 한다.
    # node1의 부모만 바꿀 경우 연결이 끊긴다.
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def dfs(node):
    neighbors = arr[node]

    for neighbor in neighbors:
        # 부모가 다르다. 즉, 다른 그래프이다
        if find(node) != find(neighbor):
            union(node, neighbor)
            dfs(neighbor)


n, m = map(int, input().split(" "))
arr = [[] for i in range(n + 1)]
parent = [i for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split(" "))
    arr[a].append(b)
    arr[b].append(a)

for i in range(n):
    dfs(i)

result = set(parent)
print(len(result) - 1)