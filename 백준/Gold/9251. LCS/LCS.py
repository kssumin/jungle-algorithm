x = input()
y = input()

x_len = len(x)
y_len = len(y)

# 여기에는 LCS의 개수
arr = [[0 for _ in range(x_len + 1)] for _ in range(y_len + 1)]
for i in range(1, y_len + 1):
    for j in range(1, x_len + 1):
        # 마지막 문자가 같다면
        if y[i - 1] == x[j - 1]:
            arr[i][j] = arr[i - 1][j - 1] + 1

        # 두 마지막 문자가 다르다면
        # j의 새로운 문자를 더하기 이전의 LCS값과
        # i의 새로운 문자를 더하기 이전의 LCS값을 비교한다
        else:
            arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
print(arr[y_len][x_len])