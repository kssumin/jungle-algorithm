"""
왜 틀렸을까?

"""


def bfs(node):
    queue = []
    queue.append(node)

    color[node] = 0

    while queue:
        start_node = queue.pop(0)

        for next_node in arr[start_node]:
            if not validate_color(start_node, next_node):
                return "NO"

            if color[next_node] == -1:
                color[next_node] = (color[start_node] + 1) % 2

            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True

    return "YES"


def validate_color(node1, node2):
    if color[node1] == color[node2]:
        return False
    return True


def is_all_right(result):
    for r in result:
        if r == "NO":
            return r

    return "YES"


k = int(input())

for _ in range(k):
    v, e = map(int, input().split(" "))
    arr = [[] for _ in range(v + 1)]
    visited = [False for _ in range(v + 1)]
    color = [-1 for _ in range(v + 1)]
    result = []

    for _ in range(e):
        a, b = map(int, input().split(" "))
        arr[a].append(b)
        arr[b].append(a)

    for i in range(1, v + 1):
        if not visited[i]:
            result.append(bfs(i))
    
    print(is_all_right(result))