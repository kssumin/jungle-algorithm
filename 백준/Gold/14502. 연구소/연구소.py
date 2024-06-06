import sys
import copy

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
VIRUS = 2
WALL = 1
SUCCESS = 0

# 바이러스를 뿌린다
def spread(maps, N, M):
    global answer
    queue = []
    visited = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if maps[i][j] == VIRUS:
                queue.append((i,j))
                visited[i][j] = WALL

    # 뿌린다
    while queue:
        x, y = queue.pop(0)

        for d in direction:
            next_x = x + d[0]
            next_y = y + d[1]

            if can_not_go(visited, maps, next_x, next_y, N, M):
                 continue

            maps[next_x][next_y] = VIRUS
            queue.append((next_x, next_y))
            visited[next_x][next_y] = 1

    # print(maps)


    # 안전 구역의 갯수를 구한다
    result = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == SUCCESS:
                result += 1
    # print(result)
    # print("=====================")

    # 안전구역 최댓값으로 갱신
    if answer < result:
        answer = result

def can_not_go(visited, maps, next_x, next_y, N,M):
    if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
        return True
    if visited[next_x][next_y] == 1:
        return True
    if maps[next_x][next_y] == WALL:
        return True
    return False

# 벽을 세운다
def set_wall(maps, count):
    if count == 3:
        maps_copy = copy.deepcopy(maps)
        # print(maps)
        spread(maps_copy, N, M)
        return

    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                maps[i][j] = 1
                set_wall(maps, count+1)
                maps[i][j] = 0


if __name__ == "__main__":
    # N : 세로, M : 가로
    N,M = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    # 벽 세울 때는 dfs를 이용한다
    set_wall(maps, 0)

    print(answer)
