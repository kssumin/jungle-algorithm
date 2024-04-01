"""
틀렸습니다....
"""


def find(node):
    if parent[node] == node:
        return node
    return find(parent[node])


def union(node1, node2):
    a = find(node1)
    b = find(node2)

    if a > b:
        parent[b] = a
    else:
        parent[a] = find(b)


def kruskal(queue, answer):
    while queue:
        node = queue.pop(0)

        node1 = node[0]
        node2 = node[1]
        weight = node[2]

        # 두 개의 부모가 다르다면 즉 다른 그래프라면
        if find(node1) != find(node2):
            answer += weight
            union(node1, node2)
    return answer


v, e = map(int, input().split(" "))
queue = []
parent = [i for i in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split(" "))
    queue.append([a, b, c])

queue.sort(key=lambda x: x[2])

print(kruskal(queue, 0))