def solution(cards):
    # 사이클 크기를 저장할 리스트
    cycle_sizes = []

    # 방문 여부를 체크하는 리스트
    visited = [False] * len(cards)
    
    def dfs(i):
        count = 0
        while not visited[i]:
            visited[i] = True
            i = cards[i] - 1
            count += 1
        return count

    for i in range(len(cards)):
        if not visited[i]:
            cycle_size = dfs(i)
            cycle_sizes.append(cycle_size)

    # 두 개 이상의 사이클이 있는 경우, 사이클 크기들을 내림차순 정렬하여 가장 큰 두 개의 사이클 크기를 곱함
    if len(cycle_sizes) > 1:
        cycle_sizes.sort(reverse=True)
        return cycle_sizes[0] * cycle_sizes[1]
    
    # 사이클이 하나만 있거나 없는 경우, 0을 반환
    return 0
