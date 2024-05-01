def solution(phone_book):
    answer = True
    
    phone_book.sort()
    # print(phone_book)
    
    for i in range(len(phone_book)-1):
        prefix = phone_book[i]
        if phone_book[i+1].startswith(prefix):
            answer=False
            break
    
    return answer