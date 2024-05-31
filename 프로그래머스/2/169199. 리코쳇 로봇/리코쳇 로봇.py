dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = []

def solution(board):
    row = len(board[0])
    column = len(board)
    
    visited = [[False for _ in range(row)] for _ in range(column)]
    distances = [[-1 for _ in range(row)] for _ in range(column)]
    
    for i in range(column):
        for j in range(row):
            if board[i][j] == 'R':
                visited[i][j] = True
                distances[i][j] = 0
                queue.append((i, j))
                answer = search(board, visited, distances, column, row)
                return answer if answer != -1 else -1
    
    return -1

def search(board, visited, distances, column, row):
    while queue:
        i, j = queue.pop(0)
        
        for k in range(4):
            next_x, next_y = i, j
            while True:
                next_x = next_x + dx[k]
                next_y = next_y + dy[k]
        
                if is_not_range(next_x, next_y, column, row):
                    next_x, next_y = next_x - dx[k], next_y - dy[k]
                    break
        
                if can_not_go(next_x, next_y, board):
                    next_x, next_y = next_x - dx[k], next_y - dy[k]
                    break
            
            if not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                distances[next_x][next_y] = distances[i][j] + 1
                queue.append((next_x, next_y))
        
                if board[next_x][next_y] == 'G':
                    return distances[next_x][next_y]
    
    return -1

def is_not_range(i, j, column, row):
    if i >= column or j >= row or i < 0 or j < 0:
        return True
    return False

def can_not_go(i, j, board):
    if board[i][j] == 'D':
        return True
    return False