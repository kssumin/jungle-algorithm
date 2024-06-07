def solution(n, computers):
    answer = 0
    network = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                network[i].append(j)
    visited = [0 for _ in range(n)]
    
    # print(network)
    for k in range(n):
        if visited[k] == 0:
            bfs(k, network, visited)
            answer+=1
    
    return answer

def bfs(k, network, visited):
    queue = []
    
    queue.append(k)
    visited[k] = 1
    
    while(queue):
        cur = queue.pop(0)
        
        for next in network[cur]:
            if visited[next] == 0:
                queue.append(next)
                visited[next] = 1
            
        
    
        