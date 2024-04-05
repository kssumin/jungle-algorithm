t = int(input())

for _ in range(t):
    n = int(input())

    coin = [0]
    coin.extend(list(map(int, input().split(" "))))

    # 목표 금액
    target = int(input())

    # 각각의 목표 금액에 대해서 해당 코인까지 적용시켰을 때의 개수
    # dp[2][4] : 목표 금액이 4일 때 2번째 코인까지 고려했을 때의 가짓수
    dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]

    # 코인이 하나밖에 없을 때 목표 금액을 맞출 수 있는 최소숫자
    for j in range(0, target + 1):
        # 첫 번째 코인으로 목표 금액을 만들 수 있는 경우
        if j % coin[1] == 0:
            dp[1][j] = 1

        else:
            dp[1][j] = 0

    # 코인이 하나밖에 없을 때 목표 금액을 맞출 수 있는 최소숫자
    for i in range(0, n + 1):
        # 첫 번째 코인으로 목표 금액을 만들 수 있는 경우
        dp[i][0] = 1

    # 코인을 하나씩 적용 시킨다
    for i in range(2, n + 1):
        # 목표 금액을 하나씩 늘린다
        for current_target in range(1, target + 1):

            # 현재 적용시키고자 하는 코인
            current_coin = coin[i]

            # 현재 적용시키고자 하는 코인이 목표 타겟보다 작다
            if current_coin > current_target:
                dp[i][current_target] = dp[i - 1][current_target]

            else:
                # 현재 코인까지 포함해서 타겟 코인을 채우려고 한다.
                # 현 코인을 적용시키지 않았을 때 값
                # 현 코인을 적용시켰을 때
                dp[i][current_target] = dp[i - 1][current_target] + dp[i][current_target - current_coin]
                
                """"
                목표 금액보다 현재 넣고자 하는 코인의 값이 더 적다.
                그러면 현 코인을 적용시킬지 안 시킬지 고민한다
                """

    # target만큼의 코인을 만들기 위해서 n번째 coin 까지 고려했을 때의 갯수
    print(dp[n][target])