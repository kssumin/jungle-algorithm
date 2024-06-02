import queue

def bfs():
    while (q.qsize() !=0):
        curr, count = q.get()

        if curr == G:
            return count

        # 위로 올라가는 거 범위 내 인지 확인
        if is_range(curr + U) and not visited[curr+U]:
            visited[curr + U] = 1
            q.put((curr + U, count + 1))
            # dp[x+U] = dfs(x+U, count+1)

        # 아래로 내려가는 거 범위 내 인지 확인
        if is_range(curr - D) and not visited[curr-D]:
            visited[curr - D] = 1
            q.put((curr - D, count + 1))
            # dp[x-D] = dfs(x-D, count+1)

    return -1


def is_range(x):
    if 1<=x<=F:
        return True
    return False

if __name__ == "__main__":
    F, S, G, U, D = map(int, input().split())
    visited = [0 for _ in range(F + 1)]
    # dp = [0 for _ in range(F+1)]
    q = queue.Queue()
    q.put((S, 0))
    visited[S] = 1
    result = bfs()

    if result == -1:
        print("use the stairs")
    else:
        print(result)
