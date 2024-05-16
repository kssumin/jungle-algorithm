from collections import deque

def solution(s):
    answer = 0
    
    q = deque(s)
    size = len(s)
    
    while(size !=0):
        # 이 부분이 하나씩 완쪽으로 회전시키는 부분
        item = q.popleft()
        q.append(item)
        
        # 해당 문자열이 올바른지 확인하는 부분
        if(check(q, len(q))):
            answer+=1
        
        size-=1
        
    return answer

def check(q, size):
    stack = []
    
    for i in range(len(q)):
        item = q[i]
        # 여는 괄호라면
        if item =='[' or item=='(' or item=='{':
            stack.append(item)
        # 닫는 괄효라면
        else:
            # 스택이 비어있다면 즉, 여는 괄호가 없을 경우는 짝이 맞지 않는다
            if not stack:
                return False
            
            item_pop = stack.pop()
            
            if item_pop=='[' and item ==']':
                continue
            if item_pop=='(' and item ==')':
                continue
            if item_pop=='{' and item =='}':
                continue
            
            return False
    
    # 스택이 비어있다면 짝이 맞는거다
    if not stack:
        return True
    return False
        
            