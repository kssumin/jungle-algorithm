n = int(input())
arr = []

for _ in range(n):
    values = input().split(" ")

    start = int(values[0])
    end = int(values[1])

    arr.append([start, end])

arr.sort(key=lambda x: (x[1], x[0]))

result = 0
last_end = 0

for a in arr:
    start_time = a[0]
    end_time = a[1]
    # 이전 회의시간이 지났다
    if start_time >= last_end:
        result += 1
        last_end = end_time

print(result)