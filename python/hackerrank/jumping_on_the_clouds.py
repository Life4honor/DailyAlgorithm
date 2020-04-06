# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

def jumpingOnClouds(c):
    position = 0
    jumps = 0
    destination = len(c) - 1

    while position < destination:
        position += 2 if position + 2 <= destination and c[position + 2] == 0 else 1
        jumps += 1

    return jumps
