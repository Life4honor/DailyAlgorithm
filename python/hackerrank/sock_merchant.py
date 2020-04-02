# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def sockMerchant(n, ar):
    number_of_socks = {}
    
    for sock in ar:
        if sock not in number_of_socks:
            number_of_socks[sock] = 0
        number_of_socks[sock] += 1
    
    return sum([number_of_socks[sock] // 2 for sock in number_of_socks])

