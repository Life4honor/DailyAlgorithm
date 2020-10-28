# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

def catAndMouse(x, y, z):
    a_dist = abs(x-z)
    b_dist = abs(y-z)

    if a_dist > b_dist:
        return "Cat B"

    if a_dist < b_dist:
        return "Cat A"

    if a_dist == b_dist:
        return "Mouse C"
