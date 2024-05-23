from collections import deque

def solution(people, limit):
    answer = 0
    
    people.sort(reverse=True)
    queue = deque(people)
    
    while(queue):
        if len(queue) == 1:
            answer+=1
            break
            
        # 2명 태울 수 있는 경우
        if queue[0] + queue[-1] <= limit:
            answer+=1
            queue.pop()
            queue.popleft()
        
        # 무거운 한 명 밖에 못 태운 경우
        else:
            answer+=1
            queue.popleft()

    return answer