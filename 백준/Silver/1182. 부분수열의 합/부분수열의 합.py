import sys


def get(current_index, sum):
    global count
    # 종료조건 : 인덱스를 넘어갔을 때
    if current_index >= n:
        return 0
    
    # 우선 현 인덱스 값을 더해주고 나중에 현 인덱스 값을 포함하지 않을 거면 그떄 뺀다
    # 이걸 안 하니깐 정답값이 0일 때 무조건 if문 조건에 걸려서 count가 엄청 증가
    sum += arr[current_index]
    if sum == s:
        count += 1

    # 현 인덱스를 포함한다.
    get(current_index + 1, sum)
    # 현 인덱스 값을 포함하지 않는다.
    get(current_index + 1, sum - arr[current_index])


if __name__ == "__main__":
    values = sys.stdin.readline().rstrip().split(" ")
    n = int(values[0])
    s = int(values[1])
    arr = []

    numbers = sys.stdin.readline().rstrip().split(" ")
    for i in range(n):
        arr.append(int(numbers[i]))

    count = 0
    get(0, 0)

    print(count)