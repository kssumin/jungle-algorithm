# 0 : 벽 , 1: 갈 수 있음
distance = [(0,1),(0,-1),(-1,0),(1,0)]

def solution(maps):
    answer = 0
    
    r = len(maps)
    c = len(maps[0])
    
    visit = [[0 for _ in range(c)] for _ in range(r)]
    queue =[]
    
    queue.append((0,0,0))
    visit[0][0] = 1
    
    while(queue):
        x, y, d = queue.pop(0)
        
        if x == r-1 and y == c-1:
            return d+1
        
        for di in distance:
            new_x = x + di[0]
            new_y = y + di[1]
            
            if can_not_go(new_x, new_y, c, r, visit, maps):
                continue
            
            visit[new_x][new_y] = 1
            queue.append((new_x, new_y, d+1))
    return -1

def can_not_go(x,y,c,r, visit, maps):
    if x<0 or x>=r or y<0 or y>=c:
        return True
    if visit[x][y] == 1:
        return True
    if maps[x][y] == 0:
        return True
    return False
