import sys

city_count = int(sys.stdin.readline().rstrip())
arr = [[] for _ in range(city_count)]
answer = sys.maxsize
visited = [0] * (city_count)


def dfs(start, now, sum):
    global answer
    # 모두 방문 했다면 시작지점을 다시 방문한다
    if isAllVisited():
        # 시작지점을 방문하지 못 하는 경우
        if arr[now][start] <= 0:
            return
        # 시작지점을 다시 방문할 수 있는 경우
        # 시작지점을 더한다
        sum += arr[now][start]

        # 최솟값 갱신 가능여부를 확인한다.
        if answer > sum:
            answer = sum
        return

    # 모두 방문하지 않았지만 현재까지 합이 현 최솟값보다 크다
    if sum >= answer:
        return

    # i는 다음 방문 후보지
    for i in range(city_count):
        # 다음 방문 후보지가 아직 방문하지 않았고
        # 0보다 크다면 즉 방문할 수 있다면
        if not visited[i] and arr[now][i] > 0:
            # 방문 처리를 한다.
            visited[i] = True
            sum += arr[now][i]
            # 방문 후보지부터 다시 시작지점으로 시작한다.
            dfs(start, i, sum)
            sum -= arr[now][i]
            visited[i] = False


def isAllVisited():
    for i in range(city_count):
        # 방문 하지 않았다면
        if not visited[i]:
            return False
    return True


if __name__ == '__main__':
    # 배열값 초기화
    for i in range(city_count):
        input_values = sys.stdin.readline().rstrip().split(" ")
        for j in range(city_count):
            arr[i].append(int(input_values[j]))

    # 첫 시작지점 선택을 위함
    for j in range(city_count):
        visited[j] = True
        dfs(j, j, 0)
        visited[j] = False

    print(answer)
