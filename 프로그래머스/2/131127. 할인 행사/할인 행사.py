def solution(want, number, discount):
    answer = 0
    
    wants = []
    
    for a, b in zip(want, number):
        print(a,b)
        for _ in range(b):
            wants.append(a)
    
    wants.sort()
    # print("wants" , wants)
    
    
    size = len(discount)
    loop  = size-9
    
    for i in range(loop):
        temp = discount[i:i+10]
        temp.sort()
        # print(i, "일", "구매", temp)
        
        if temp == wants:
            answer+=1   
    return answer