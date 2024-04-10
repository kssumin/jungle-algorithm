n, k = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
plug = []
result = 0

for i in range(k):
    current = arr[i]

    # 현 전기용품이 멀티탭에 있다
    if current in plug:
        continue

    # 아직 플러그가 채워져있지 않으면 넣는다
    if len(plug) < n:
        plug.append(current)
        continue

    # 현 플러그에 있는 아이템이 최근에 들어오면 플러그에서 삭제하지 않는다
    # 현 플러그에 있는 아이템이 나중에 들어오거나/들어오지 않으면 플러그에서 삭제한다

    left = arr[i + 1:len(arr)]
    index = 0
    replaced = False

    for item in plug:
        # 조건 1. 앞으로 나타나지 않는다.
        if item not in left:
            plug.remove(item)
            plug.append(current)
            result += 1
            replaced = True
            break

        else:
            # 나타나는 경우 나타나는 순서를 알아낸다
            come_index = left.index(item)

            # 나타나는 인덱스가 늦을 수록 해당 인덱스에 있는 값으로 교체한다
            if come_index > index:
                index = come_index

    # 조건 2. 가장 늦게 나타나는 아이템으로 교체한다
    if not replaced:
        change_item = left[index]
        plug.remove(change_item)
        plug.append(current)
        result += 1

print(result)