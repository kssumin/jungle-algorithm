import sys

"""
버블 정렬 이용하기
* swap이 많이 일어난다.
* 주어진 배열이 차지하고 있는 공간내에서 값들의 위치만 바꾼다.
  => 따라서 공간복잡도는 O(1)이다.
* 루프문을 통해서 모든 인덱스에 접근해야 한다. => O(n)
  또한 하나의 루프에서느 인접한 값들의 대소비교 및 swap이 일어나야 한다. => O(n)
  따라서 총 시간복잡도는 O(n^2)이다.
"""


def bubble_sort(arr):
    # 비교를 할 총 배열 범위
    for i in range(len(arr) - 1, 0, -1):

        # 각 배열의 앞에서부터 비교를 한다.
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == "__main__":
    reply = int(sys.stdin.readline().rstrip())
    arr = []

    for i in range(reply):
        arr.append(int(sys.stdin.readline().rstrip()))

    answer = bubble_sort(arr)

    for i in range(len(answer)):
        print(answer[i])