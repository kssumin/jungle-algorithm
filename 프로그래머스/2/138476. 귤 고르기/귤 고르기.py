from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    counter = Counter(tangerine)
    # 빈도가 많은 element부터 출력되도록 정렬
    values = counter.most_common()
      
    for value in values:
        k = k-value[1]
        answer+=1
        if k >0:
            continue

        else:
            break        
       
    return answer