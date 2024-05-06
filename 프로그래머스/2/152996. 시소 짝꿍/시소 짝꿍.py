from collections import Counter

def solution(weights):
    answer = 0
    
    counter = Counter(weights)
    
    max_value = max(weights)
    min_value = min(weights)
        
    for weight in range(min_value, max_value+1):
        # 해당 몸무게가 존재한다면
        if counter[weight] >= 1:
            self_weight = counter[weight] 
            
            answer = answer + (counter[weight * (2/3)] * self_weight)
            answer = answer + (counter[weight * (1/2)] * self_weight)
            answer = answer + (counter[weight * (3/4)] * self_weight)
                  
            answer = answer + ((self_weight * (self_weight -1))//2)

            
    return answer