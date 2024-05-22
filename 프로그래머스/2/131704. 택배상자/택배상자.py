def solution(order):
    answer = 0
    
    container = [i for i in range(1, len(order)+1)]
    temp_c = []
    
    index = 0
    
    print(container)
    print(container.pop(0))
    print(container)
    
    stack=[1,2,3]
    print(stack)
    print(stack.append(4))
    print(stack)
#     while(true):
#         # 컨테이너는 모두 다 봤을 때 이제 임시 컨테이너만 봐야함
#         if index >= len(order):
#             return answer
        
#         # 컨테이너도 볼 상자가 남음
#         else:
#             # 컨테이너에 현 주문이 있음
#             if container[0] == order[0]:
#                 answer+=1
            
#             # 임시컨테이너에 현 주문이 있음
#             elif temp_c[0] == order[0]:
#                 temp_c.pop(0)
#                 answer+1
            
#             # 임시 컨테이너와 컨테이너 모두 현 주문이 없음
#             else:
#                 temp_c.append(container.pop(0))
                
        
        
        
    
    return answer