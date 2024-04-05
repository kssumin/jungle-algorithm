n, max_bag_weight = map(int, input().split(" "))

# (무게, 가치)
stuff = [[0, 0]]

# 각각의 배낭 크기에 대한 물건의 가치의 최대값을 모아둔다.
# dp[2][4] : 가방의 최대 무게가 4일 때 2번째 물건까지 고려했을 때의 최대가치값
dp = [[0 for _ in range(max_bag_weight + 1)] for _ in range(n + 1)]

for _ in range(n):
    stuff.append(list(map(int, input().split(" "))))

# 물건을 하나씩 넣어본다
for i in range(1, n + 1):
    # 무게가 1일 때부터 계산한다
    for current_bag_weight in range(1, max_bag_weight + 1):
        weight = stuff[i][0]
        value = stuff[i][1]

        # 배낭의 최대 무게가 현 물건의 무게보다 작다
        # 배낭에 현 물건을 넣지 못 한다
        if current_bag_weight < weight:
            # 현 물건을 고려하기 이전의 최대 가치값과 동일하다
            dp[i][current_bag_weight] = dp[i - 1][current_bag_weight]

        # 배낭의 최대 무게가 현 물건의 무게보다 크거나 같다
        # 해당 물건을 넣을 수는 있다.
        # 그렇다면 해당 물건을 넣을지 말지 결정한다.
        else:
            # 현 물건을 넣지 않았을 경우 최대 가치값과
            # 현 물건을 넣었을 때의 가치값을 비교한다
            dp[i][current_bag_weight] = max(dp[i - 1][current_bag_weight], value + dp[i - 1][current_bag_weight - weight])

# k의 최대 무게를 가지는 백팩에 n번째 물건까지 고려했을 때의 최대가치
print(dp[n][max_bag_weight])