# https://www.hackerrank.com/challenges/counting-valleys/problem

def countingValleys(n, s):
    nums_of_valleys = 0
    level = 0
    first_step = []

    for step in s:
        if first_step == []:
            first_step.append(step)

        if step == 'U':
            level += 1

        if step == 'D':
            level -= 1

        if level == 0 and first_step.pop() == 'D':
            nums_of_valleys += 1

    return nums_of_valleys
