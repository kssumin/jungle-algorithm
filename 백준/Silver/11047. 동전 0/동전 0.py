n, k = map(int, input().split(" "))
arr = []
result = 0

for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in arr:
    if k == 0:
        break
    # 총 만들어야 할 금액이 더 작다면
    if k < i:
        continue

    result += (k // i)
    k = k % i


print(result)