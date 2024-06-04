def solution(maps):
    d1 = bfs('S', 'L', maps)
    d2 = bfs('L', 'E', maps)
       
    if d1 == -1 or d2 == -1:
        return -1
    
    return d1 + d2
    
               
def bfs(start, end, maps):
    row = len(maps)
    column = len(maps[0])
    
    queue = []
    # 새로 visited 테이블을 갱신해주고 있음
    visited = [[0 for _ in range(column)] for _ in range(row)]
    
    for i in range(row):
        for j in range(column):
            # 시작지점 발견
            if maps[i][j] == start:
                visited[i][j]=1
                queue.append((i,j,0))
                return answer(maps, queue, visited, end, column, row)

def answer(maps, queue, visited, end, column, row):
    direction = [(0,1),(0,-1),(1,0), (-1,0)]
    
    while(queue):
        i,j,t_d = queue.pop(0)
            
        for d in direction:
            
            next_x, next_y = i + d[0], j + d[1]
             
            if can_not_visited(next_x, next_y,column, row, maps, visited):
                continue
            
            if maps[next_x][next_y] == end:
                return t_d + 1
            
            visited[next_x][next_y]=1
            queue.append((next_x,next_y, t_d + 1))
            
    return -1
        
# def can_not_visited(i,j, column, row, maps, visited):
#     # 범위를 벗어났다면
#     if i < 0 or i >= column or j < 0 or j>= row:
#         return True
#     # 벽이 아니면서 아직 방문하지 않았다면
#     if maps[i][j] == 'X' or visited[i][j]==1:
#         return True
#     return False

def can_not_visited(i, j, column, row, maps, visited):
    if i < 0 or i >= row or j < 0 or j >= column:
        return True
    if maps[i][j] == 'X' or visited[i][j] == 1:
        return True
    return False

        