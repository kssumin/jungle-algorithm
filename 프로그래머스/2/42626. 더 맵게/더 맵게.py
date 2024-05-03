import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while(True):
        # scoville.sort()
        min = heapq.heappop(scoville)
        
        if len(scoville) == 0:
            if min >=K:
                return answer
            return -1
        
        
    # 기준에 만족하지 못 하는 경우    
        if min<K:
            answer +=1
            second_min = heapq.heappop(scoville)
            
            # print("answer", answer)
            # print("scovile", scoville)
            
            cal = min + (second_min*2)
            
            heapq.heappush(scoville, cal)
        
        if min>=K:
            return answer
        
    
    return answer