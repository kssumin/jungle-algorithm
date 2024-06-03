def solution(data, col, row_begin, row_end):
    answer = 0
    
    # col 기준 정렬
    data.sort(key = lambda x:(x[col-1], -x[0]))

    # 기본키 기준 정렬
    # for i in range(len(data)-1):
    #     j = i+1
    #     if data[i][col-1] == data[j][col-1] and data[i][0] < data[j][0]:
    #         data[i], data[j] = data[j], data[i]
    
    # print(data)
    
    # t = 0

    for i in range(row_begin - 1, row_end):
        t=0
        for j in range(len(data[0])):
            t = t + (data[i][j] % (i+1))
        
        if i == row_begin -1:
            answer = t
        else:
            answer = (answer ^ t)
        
        
    return answer