N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N

"""
현재의 값을 이전 값들과 비교한다
"""
for current_node in range(1, N):
    for compare_node in range(current_node):
        """
        현재 삽입하려는 노드의 값이 비교하는 값보다 더 크다 -> 증가하는 수열로 만들 수 있다.
        """
        
        if arr[compare_node] < arr[current_node] and dp[current_node] <= dp[compare_node]:
            dp[current_node] = dp[compare_node] + 1

print(max(dp))