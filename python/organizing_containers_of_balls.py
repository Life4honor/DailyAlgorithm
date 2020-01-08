# https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem

def organizingContainers(container):
    available = [0] * len(container)
    type_cnt = [0] * len(container)
    for idx, row in enumerate(container):
        available[idx] = sum(row)
        for types, cnt in enumerate(row):
            type_cnt[types] += cnt

    if sorted(available) == sorted(type_cnt):
        result = "Possible"
    else:
        result = "Impossible"
    
    return result
