# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    index_price = {}
    flag = {}
    length = len(prices)
    result = [0] * length
    
    for idx, price in enumerate(prices):
        index_price[idx] = price
        flag[idx] = True
        
    for idx, price in enumerate(prices):
        pos = idx + 1
            
        while flag[idx] and pos < length:
            if index_price[pos] < price:
                flag[idx] = False
            
            result[idx] += 1
            pos += 1
            
    return result