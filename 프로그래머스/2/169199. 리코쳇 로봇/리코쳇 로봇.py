dx = [-1,1,0,0]
dy=[0,0,-1,1]

def solution(board):
    answer = 0
    
    row = len(board[0])
    column = len(board)
    
    visited = [[False for _ in range(column)] for _ in range(row)]
    
    print(visited)
    print(row, column)
    print(board[0][1])
    
    
    for i in range(row):
        for j in range(column):
            if board[i][j] == 'G':
                dfs(i,j)
    
    return answer


def dfs(i,j):
    for k in range(4):
        new_x = i + dx[k]
        new_y = i + dy[k]
        
        if is_not_range(new_x, new_y):
            continue
        


def is_not_range(i,j):
    global column, row
    if i>=column or j>=row:
        return true
    return false