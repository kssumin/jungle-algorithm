from collections import deque


def bfs():
    # (현재까지의 총합, 동전 개수 총합)
    queue = deque()

    for coin in coins:
        if coin > k:
            continue
        queue.append((coin, 1))
        visited[coin] = True
        # 해당 coin 가치를 만드는데 필요한 최소 동전 수라는 것을 보장할 수 있다.
        dp[coin] = 1

    while queue:
        value, count = queue.popleft()
        if value == k:
            return count

        for coin in coins:
            # 가치를 넘는다면 패스
            if value + coin > k:
                continue
            # 가치와 동일하거나 가치에 못 미친다면
            # 해당 가치를 방문한 이력이 있는지 확인
            # 방문한 적이 있으면 해당 값이 최소이다
            if not visited[value + coin]:
                current_coin_count = count + 1
                queue.append((value + coin, current_coin_count))
                visited[value + coin] = True
                dp[value + coin] = current_coin_count

            # 이미 해당 가치를 방문했다면 더 최솟값이 있다는 뜻이다
            # 따라서 더 이상 큐에 넣어서 진행하지 않는다

    return -1


n, k = map(int, input().split())
coins = set(int(input()) for _ in range(n))
visited = [0 for _ in range(k + 1)]
dp = [0 for _ in range(k + 1)]
dp[0] = 0

print(bfs())