from collections import deque

def solution(queue1, queue2):
    max = len(queue1) + len(queue2) 
    answer = 0
    
    # 우선 반이 안 되는지 확인
    if (sum(queue1) + sum(queue2)) % 2 != 0:
        return -1
    
    while(sum(queue1) != sum(queue2)):
        if answer > max:
            return -1
    
    
        if sum(queue1) > sum(queue2):
            item = queue1.pop(0)
            queue2.append(item)
            answer+=1
            
        else:
            item = queue2.pop(0)
            queue1.append(item)
            answer+=1
    
    return answer
            
            
        