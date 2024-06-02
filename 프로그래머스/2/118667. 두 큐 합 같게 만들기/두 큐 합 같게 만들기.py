from collections import deque

def solution(queue1, queue2):
    # 큐를 deque로 변환하여 효율적인 pop, append 연산을 사용
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total_sum = sum1 + sum2
    
    # 전체 합이 홀수면 반으로 나눌 수 없으므로 -1 반환
    if total_sum % 2 != 0:
        return -1
    
    target = total_sum // 2
    max_operations = 3 * len(queue1)
    operations = 0
    
    while sum1 != target and operations <= max_operations:
        if sum1 > target:
            # queue1의 앞에서 요소를 제거하여 queue2에 추가
            item = queue1.popleft()
            sum1 -= item
            queue2.append(item)
        else:
            # queue2의 앞에서 요소를 제거하여 queue1에 추가
            item = queue2.popleft()
            sum2 -= item
            queue1.append(item)
            sum1 += item
        operations += 1
    
    return operations if sum1 == target else -1
