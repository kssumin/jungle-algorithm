t = int(input())

for _ in range(t):
    arr = []
    result = 1
    n = int(input())

    for _ in range(n):
        values = list(map(int, input().split(" ")))
        arr.append((values[0], values[1]))
        
    # 서류 점수를 기준으로 정렬한다
    arr.sort(key=lambda x: x[0])

    top = arr[0][1]

    # 서류 점수 2등부터 시작한다
    for target in range(1, len(arr)):
        # 현 지원자의 면접 등수가 더 낮다
        if arr[target][1] < top:
            # 가장 높은 등수를 변경한다
            top = arr[target][1]
            result += 1
    print(result)