def solution(words, queries):
    cache = {}
    answer = []
    
    for query in queries:
        if query in cache:
            answer.append(cache[query])
            continue
            
        searched_cnt = search(words, query)
        answer.append(searched_cnt)
        cache[query] = searched_cnt
        
    return answer

def search(words, query):
    cache = {}
    length = len(query)
    suff, pref = None, None
    
    if query == "?"*length:
        return len([word for word in words if len(word) == length])
    elif query.startswith('?'):
        suff = query[length - query[::-1].index('?'):]
    else:
        pref = query[:query.index('?')]
    
    cnt = 0
    for word in words:
        if word in cache:
            cnt += 1
            continue
            
        if length != len(word):
            continue
            
        if pref is not None and word.startswith(pref):
            cnt += 1
            cache[word] = True
            continue
            
        if suff is not None and word.endswith(suff):
            cnt += 1
            cache[word] = True
            continue
        
    return cnt
