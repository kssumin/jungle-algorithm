import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

WATER = "*"
GROUND = "."
ROCK = "X"
CAVE = "D"


def bfs(node_x, node_y, answer):
    queue = []
    queue.append((answer, node_x, node_y))
    visited[node_x][node_y] = True

    while queue:
        go_water()
        queue_len = len(queue)
        while queue_len:
            answer, node_x, node_y = queue.pop(0)

            for i in range(4):
                next_x, next_y = node_x + dx[i], node_y + dy[i]

                if not_range(next_x, next_y):
                    continue

                # 도착지점
                if is_end(next_x, next_y):
                    return answer + 1

                if cannot_go(next_x, next_y):
                    continue

                # 검은색이 아닐 경우 새롭게 바꾸지 않아도 된다.
                visited[next_x][next_y] = True
                arr[next_x][next_y] = "S"
                queue.append((answer + 1, next_x, next_y))

            queue_len -= 1

    return "KAKTUS"


def go_water():
    water_search_count = len(water_queue)

    while water_search_count:
        water_x, water_y = water_queue.pop(0)

        for j in range(4):
            next_water_x, next_water_y = water_x + dx[j], water_y + dy[j]
            if cannot_go_water(next_water_x, next_water_y):
                continue

            # 갈 수 있다면 넣는다.
            arr[next_water_x][next_water_y] = WATER
            water_queue.append((next_water_x, next_water_y))

        water_search_count -= 1


def cannot_go_water(x, y):
    if not_range(x, y):
        return True
    if arr[x][y] == ROCK or arr[x][y] == WATER or arr[x][y] == CAVE:
        return True
    return False


def not_range(next_x, next_y):
    if next_x < 0 or next_x >= r or next_y < 0 or next_y >= c:
        return True
    return False


def is_end(next_x, next_y):
    if arr[next_x][next_y] == "D":
        return True
    return False


def cannot_go(next_x, next_y):
    # 물과 돌맹이는 가지 못 한다
    if arr[next_x][next_y] == WATER or arr[next_x][next_y] == ROCK:
        return True
    if validate_already_go(next_x, next_y):
        return True
    return False


def validate_already_go(next_x, next_y):
    return visited[next_x][next_y]


r, c = map(int, input().split(" "))
arr = [[0 for _ in range(c)] for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]
start_x, start_y = 0, 0

water_queue = []
water_search_count = 0

for i in range(r):
    values = input()
    for j in range(c):
        value = values[j]
        arr[i][j] = value

        if value == "S":
            start_x = i
            start_y = j

        if value == WATER:
            water_queue.append((i, j))

print(bfs(start_x, start_y, 0))