# 다음 방문할 노드는 방문하지 않은 노드 중에서 가장 짧은 길이를 가진 노드이다
def get_next_node():
    min_distance = INF
    min_distance_node = 0
    for i in range(1, n + 1):
        if not visited[i]:
            if min_distance > distance[i]:
                min_distance = distance[i]
                min_distance_node = i
    return min_distance_node


def validate_end():
    # 목적지 노드 방문 여부
    return visited[end]


def dijkstra(vertex):
    for next_node in graph[vertex]:
        next_vertex = next_node[0]
        next_weight = next_node[1]

        temp = distance[vertex] + next_weight
        if distance[next_vertex] > temp:
            distance[next_vertex] = temp

    if validate_end():
        return distance[end]
    next_value = get_next_node()
    visited[next_value] = True

    return dijkstra(next_value)


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
INF = 100000001
distance = [INF for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split(" "))
    graph[a].append([b, c])

start, end = map(int, input().split(" "))

distance[start] = 0
visited[start] = True

print(dijkstra(start))