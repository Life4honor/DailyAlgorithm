# https://www.hackerrank.com/challenges/staircase/problem

def staircase(n):
    width = n
    while n > 0:
        n -= 1
        row = ' ' * n +'#' * (width - n)
        print(row)
