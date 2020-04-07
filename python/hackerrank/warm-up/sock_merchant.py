# https://www.hackerrank.com/challenges/sock-merchant/problem

def sockMerchant(n, ar):
    number_of_socks = {}
    
    for sock in ar:
        if sock not in number_of_socks:
            number_of_socks[sock] = 0
        number_of_socks[sock] += 1
    
    return sum([number_of_socks[sock] // 2 for sock in number_of_socks])

