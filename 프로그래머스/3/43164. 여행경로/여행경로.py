def solution(tickets):
    global answer
    answer = []
    
    visited = [0 for _ in range(len(tickets))]
    tickets.sort(key = lambda x:x[1])
    
    dfs("ICN", ["ICN"], visited, tickets)

    if answer:
        return answer[0]
    else:
        return [] 

def dfs(start, path, visited, tickets):
    if len(answer)>=1:
        return
    
    if len(path) == len(tickets)+1:
        answer.append(path)
        return
    
    for idx, ticket in enumerate(tickets):
        if ticket[0] == start and not visited[idx]:
            visited[idx] = True
            dfs(ticket[1], path+[ticket[1]], visited, tickets)
            visited[idx] = False
        
    

    
    
