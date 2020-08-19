# https://www.hackerrank.com/challenges/mini-max-sum/problem

def miniMaxSum(arr):
    min_, max_ = None, None
    sum_ = sum(arr)

    for el in arr:
        if min_ is None:
            min_ = el
        if max_ is None:
            max_ = el
        
        min_ = el if min_ > el else min_
        max_ = el if max_ < el else max_
    
    print(sum_ - max_, sum_ - min_)
