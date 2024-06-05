ENTER = ("Enter", "들어왔습니다")
CHANGE = ("Change", "변경")
LEAVE = ("Leave", "나갔습니다")

def solution(record):
    answer = []
    
    history = []
    nickname={}
    
    for r in record:
        temp = r.split(" ")
        
        # 닉네임 관리
        if temp[0] == ENTER[0]:
            nickname[temp[1]] = temp[2]
            # 기록 관리
            history.append((temp[0], temp[1]))
        if temp[0] == CHANGE[0]:
            nickname[temp[1]] = temp[2]
        if temp[0] == LEAVE[0]:
            history.append((temp[0], temp[1]))
         
    for h in history:
        if h[0] == ENTER[0]:
            answer.append(nickname.get(h[1]) +"님이 들어왔습니다.")
        
        if h[0] == LEAVE[0]:
            answer.append(nickname.get(h[1])+"님이 나갔습니다.")
        
    return answer

