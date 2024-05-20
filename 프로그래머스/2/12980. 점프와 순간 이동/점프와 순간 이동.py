def solution(n):
    ans = 0
    
    ans = answer(n)

    return ans

def answer(n):
    if n == 0:
        return 0
    
    # 2로 나누어 떨어진다면
    if n % 2 == 0:
        return answer(n//2)
    else:
        return 1+answer(n-1)