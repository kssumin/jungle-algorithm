import sys

def solution(s):
    answer = 0

    size = len(s)
    loop = size // 2
    answer = sys.maxsize
    
    print(len(str(8)))
    
    for i in range(1, loop+1):
        mid_answer = size
        temp = 1
        for j in range(0, size-i, i):
            # print("값 , 다음 값", s[j:j+i], s[j+i:j+i+i])
            if s[j:j+i] == s[j+i:j+i+i]:
                temp+=1
                
                
                if j+i+i == size and temp != 1:
                    mid_answer = mid_answer - (temp * i) + (i+len(str(temp)))
                    # print("mid_answer", mid_answer)
                # print("temp", temp)  
                  
            else:
                if temp != 1:
                    mid_answer = mid_answer - (temp * i) + (i+len(str(temp)))
                    temp = 1
                
                # print("mid_answer", mid_answer)
        
        
        if answer > mid_answer:
            answer = mid_answer
    
    if size == 1:
        return size
                
    return answer
    
    
    
    