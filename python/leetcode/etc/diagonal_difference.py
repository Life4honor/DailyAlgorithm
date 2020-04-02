# https://www.hackerrank.com/challenges/diagonal-difference/problem

def diagonalDifference(arr):
    column_idx = 0
    left_to_right = 0
    right_to_left = 0
    for row in arr:
        left_to_right += row[column_idx]
        right_to_left += row[-1-column_idx]
        column_idx += 1
    
    return abs(left_to_right - right_to_left)

