# https://www.hackerrank.com/challenges/plus-minus/problem

def plusMinus(arr):
    positive_cnt = 0
    negative_cnt = 0
    zero_cnt = 0
    length = len(arr)

    for num in arr:
        if num > 0:
            positive_cnt += 1
            continue
        if num < 0:
            negative_cnt += 1
            continue
        zero_cnt += 1

    print("{:f}".format(positive_cnt/length))
    print("{:f}".format(negative_cnt/length))
    print("{:f}".format(zero_cnt/length))
