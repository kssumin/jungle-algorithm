import sys
# 큰 원반을 가장 아래에 두고 싶다.
# 그렇게 하려면 큰 원반은 목표지점에 있고, 큰 원반을 출발지점에서 빼기 위해서는 큰 원반을 제외한 나머지 원반은 출발지점도, 목표지점도 아닌 곳에 있어야 한다.
# 여기서는 이동하는 경우의 수를 모두 포함해야 한다.
# 따라서, 큰 원반을 제외한 모든 것을 출발/목표 지점이 아닌 곳에 둔다/
# 큰 원반을 목표지점에 둔다.
# 이후 다른 원반들도 목표지점에 둘 수 있도록 한다.

# 즉 큰 원반을 목표 지점의 젤 아래에 두려면, 큰 원반을 제외한 나머지를 출발/목표 지점이 아닌 곳에 두어야 한다.
# 가 핵심이다.

def hanoi(n, start, end):
    if n == 1:
        print(start,end)
        return

    # 한 개를 제외한 나머지를 나머지 장소에 둔다
    hanoi(n -1, start ,6-start-end)

    # 그 한 개를 옮긴다.
    hanoi(1, start, end)

    # 나머지 장소에 둔 것들을 다시 목표 장소로 옮긴다.
    hanoi( n-1, 6-start-end, end)

n = int(input())
from_index = 1
to_index = 3

print(2**n-1)
if n<=20:
    hanoi(n, from_index, to_index)