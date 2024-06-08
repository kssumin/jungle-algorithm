def solution(begin, target, words):
    answer = 0
    queue = []
    size = len(words)
    word_size = len(words[0])
    
    if target not in words:
          return 0
    
    queue.append((begin, 0))
    
    while(queue):
        source, result = queue.pop(0)
        
        if source == target:
            return result
        
        for word in words:
            mid = 0
            for i in range(word_size):
                if source[i] != word[i]:
                    mid+=1
            
            # 다른 게 하나인 경우에만 다음 방문 처리로 넣는다
            if mid == 1:
                queue.append((word, result+1))
                words.remove(word)
                
    return 0
    
        
                  
                  
    
    