def dfs(graph, node):
    stack = []
    result = []
    visited = [False] * (n + 1)

    stack.append(node)

    while stack:
        current_node = stack.pop()

        if not visited[current_node]:
            visited[current_node] = True
            result.append(current_node)

            next_nodes = graph[current_node]

            for next_node in reversed(next_nodes):
                if not visited[next_node]:
                    stack.append(next_node)

    return result


def dfs_recursive(result, visited, graph, node):
    if not visited[node]:
        visited[node] = True
        result.append(node)

        next_nodes = graph[node]

        for next_node in next_nodes:
            if not visited[next_node]:
                dfs_recursive(result, visited, graph, next_node)

    return result


def bfs(graph, node):
    queue = []
    result = []
    visited = [False] * (n + 1)

    queue.append(node)
    visited[node] = True

    while queue:
        current_node = queue.pop(0)
        result.append(current_node)

        next_nodes = graph[current_node]

        for next_node in next_nodes:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True

    return result


if __name__ == "__main__":
    n, m, v = map(int, input().split())

    graph = [[] for i in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in graph:
        i.sort()

    result = []
    visited = [False] * (n + 1)
    print(" ".join(map(str, dfs_recursive(result, visited, graph, v))))
    print(" ".join(map(str, bfs(graph, v))))