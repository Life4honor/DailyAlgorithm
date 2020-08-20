# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

def beautifulDays(i, j, k):
    count = 0

    for day in range(i, j+1):
        day_inv = int(str(day)[::-1])
        diff = abs(day - day_inv)
        if diff % k == 0:
            count += 1

    return count
