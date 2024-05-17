from collections import Counter

def solution(topping):
    answer = 0
    size = len(topping)
    
    arr1 = Counter(topping)
    arr2 = set()
    
    for i in topping:
        arr2.add(i)
        arr1[i]-=1
        
        if arr1[i] == 0:
            arr1.pop(i)
        
        # print("arr1", arr1)
        # print("arr1 size : ", len(arr1))
        
        
        if len(arr1) == len(arr2):
            answer+=1
    
    return answer