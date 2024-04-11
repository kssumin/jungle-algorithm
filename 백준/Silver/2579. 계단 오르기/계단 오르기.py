n = int(input())
stair = [0]
dp = [0 for _ in range(n + 1)]

for _ in range(n):
    stair.append(int(input()))

# 처음 계단은 올라야지 최댓값
if n >= 1:
    dp[1] = stair[1]

if n >= 2:
    # 두 번째 계단은 첫 번째 계단 이후에 오르는 게 최댓값
    dp[2] = dp[1] + stair[2]

if n >= 3:
    # 세 번쨰 계산은 첫 번째 계단 다음 또는 두 번째 계단 다음
    dp[3] = max(dp[1] + stair[3], stair[2] + stair[3])

# 4번째 계단이면 2번째 계단을 안 올라간 경우와 올라간 경우로 나뉜다
for i in range(4, n + 1):
    dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i])

print(dp[n])