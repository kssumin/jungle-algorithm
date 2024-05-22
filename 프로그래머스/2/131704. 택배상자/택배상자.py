def solution(order):
    answer = 0
    stack = []
    size = len(order)
    # 현 트럭에 담아야 하는 상자의 인덱스
    index = 0
    
    for box in range(1, size+1):
        stack.append(box)
        
        # 현 임시 컨테이너에 있는 것을 트럭에 담아야 한다
        while (stack and stack[-1] == order[index]):
            answer+=1
            index+=1
            stack.pop()
            
    return answer
            