"""
배낭 문제의 핵심은
해당 값은 적용시킬 것인가 말 것인가이다.
"""

for _ in range(int(input())):
    n = int(input())
    coins = list(map(int, input().split()))
    target = int(input())
    dp = [[0 for _ in range(target + 1)] for _ in range(len(coins) + 1)]

    # 0을 만들 수 있는 가지수는 1이다
    for i in range(len(coins) + 1):
        dp[i][0] = 1

    for i in range(1, len(coins) + 1):
        current_coin = coins[i - 1]
        for j in range(1, target + 1):
            if j - current_coin >= 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - current_coin]
            else:
                dp[i][j] = dp[i - 1][j]

    print(dp[len(coins)][target])