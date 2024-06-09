def solution(tickets):
    global answer
    answer = []
    graph = {}
    
    # {src : [dest...]}
    for ticket in tickets:
        src, dest = ticket
        if src not in graph:
            graph[src] = [dest]
        else:
            graph[src].append(dest)
    
    # dest 정렬
    for src in graph:
        graph[src].sort()
    
    dfs("ICN", tickets, ["ICN"], graph)
    
    return answer[0]

def dfs(src, tickets, tmp_path, graph):
    if len(answer)>=1:
        return
    
    if len(tmp_path) == len(tickets)+1:
        answer.append(tmp_path)
        return
    
    if src not in graph:
        return
    if not graph[src]:
        return
    
    for temp in range(len(graph[src])):     
        dest = graph[src].pop(0)
        dfs(dest, tickets, tmp_path+[dest], graph)
        graph[src].append(dest)
        # graph[src].sort(reverse=True)
    
    
    
    
    
