from collections import Counter

def solution(weights):
    answer = 0
    
    counter = Counter(weights)
    # print(counter)
    
    for weight, num in counter.items():
        # print(weight, num)
        answer = answer + counter[weight*(1/2)] * num
        answer = answer + counter[weight*(2/3)] * num
        answer = answer + counter[weight*(3/4)] * num
        answer = answer + ((num * (num - 1)) / 2)
        print(answer)
    return answer