# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

def rotLeft(a, d):
    move = d % len(a)
    return a[move:] + a[:move]

