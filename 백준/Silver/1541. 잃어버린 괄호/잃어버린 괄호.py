values = input()
num = []

exp = values.split("-")

for es in exp:
    e = es.split("+")
    mid_sum = 0

    for plus_item in e:
        mid_sum += int(plus_item)

    num.append(mid_sum)

result = num[0]
for i in range(1, len(num)):
    result -= num[i]

print(result)