#https://www.hackerrank.com/challenges/compare-the-triplets/problem

def compareTriplets(a, b):
    a_point, b_point = 0, 0

    for i in range(3):
        if a[i] > b[i]:
            a_point += 1
        elif b[i] > a[i]:
            b_point += 1

    return (a_point, b_point)
