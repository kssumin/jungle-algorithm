def solution(plans):
    answer = []
    stack = []
    
    # 시작 시간 기준으로 정렬
    for plan_index in range(len(plans)):
        plans[plan_index][1] = convert_minute(plans[plan_index][1])
    
    plans.sort(key = lambda x: x[1])
    
    current_time = plans[0][1]
    
    for plan_index in range(0,len(plans)):
        subject = plans[plan_index][0]
        start_time = plans[plan_index][1]
        total_time = start_time + int(plans[plan_index][2])
        
        if plan_index == len(plans)-1:
            next_start_time = int(1e9)
            
        else:
            next_start_time = plans[plan_index+1][1]
            print(next_start_time)
    
        
        # 아직 다음 과제 시작전까지 시간이 남았다.
        if current_time < start_time:
            while(len(stack)!=0):
                temp = stack.pop()
                total_rest_time = temp[1]
                
                print(temp[0], total_rest_time,"rest_time")
                
                print(current_time+total_rest_time, start_time)
                
                if current_time + total_rest_time > start_time:
                    stack.append((temp[0], (current_time + total_rest_time) - start_time))
                    current_time = start_time
                    break 
        
                else:
                    answer.append(temp[0])
                    print(answer, "answer")
                    current_time = current_time + total_rest_time
                    
        
        # 다음 과제를 시작해야 한다.
        if total_time > next_start_time:
            stack.append((subject, total_time - next_start_time))
            current_time = next_start_time
        
        else:
            answer.append(subject)
            current_time = total_time
            print(total_time, subject)
    
    
    while(len(stack)!=0):
        temp = stack.pop()
        answer.append(temp[0])
                    
    return answer


def convert_minute(start_time):
    temps = list(map(int, start_time.split(":")))
    
    return 60 * temps[0] + temps[1]