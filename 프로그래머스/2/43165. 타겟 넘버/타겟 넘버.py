def solution(numbers, target):
    return find(numbers, target, 0, 0)
    
def find(numbers, target, next_index, total):
    # 모든 숫자를 다 탐색했을 경우
    if next_index == len(numbers):
        # 원하는 숫자를 만들었을 경우
        if total == target:
            return 1
        # 원하는 숫자를 만들지 못 했을 경우
        return 0
    
    # 현재 인덱스의 숫자를 더하거나 빼는 두 가지 경우를 고려
    count_with_add = find(numbers, target, next_index + 1, total + numbers[next_index])
    count_with_subtract = find(numbers, target, next_index + 1, total - numbers[next_index])
    
    # 두 경우의 수를 합산하여 반환
    return count_with_add + count_with_subtract
