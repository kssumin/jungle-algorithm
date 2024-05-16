from collections import deque

def solution(s):
    answer = 0
    
    q = deque(s)
    size = len(s)
    
    # while(size !=0):
    #     item = q.popleft()
    #     q.append(item)
        
    if(check(q, size)):
            answer+=1
        
        # size-=1
        
    return answer

def check(q, size):
    stack = []
    
    if size == 0:
        return False

    print(q)
    print(q.popleft())
    print(q.popleft())
    
    # for i in range(size):
    #     item = q.popleft()
    #     print(item)
        # 여는 괄호라면
#         if item =='[' or item=='(' or item=='{':
#             stack.append(item)
#         # 닫는 괄효라면
#         else:
#             # 스택이 비어있다면
#             if not stack:
#                 # 여는 괄호가 없다는 뜻이므로 실패
#                 return False
            
#             # item_pop = stack.pop()
#             item_pop = 0
            
#             if item_pop=='[' and item ==']':
#                 continue
#             elif item_pop=='(' and item ==')':
#                 continue
#             elif item_pop=='{' and item =='}':
#                 continue
#             else:
#                 return False
    
#     if not stack:
#         return True
#     return False