# https://www.hackerrank.com/challenges/2d-array/problem

def hourglassSum(arr):
    position_x, position_y = 0,0
    maximum_sum = -63
    wall_x = len(arr[0])
    wall_y = len(arr)

    while position_x + 2 < wall_x:
        position_y = 0
        while position_y + 2 < wall_y:
            first_row = arr[position_y][position_x:position_x + 3]
            second_row = arr[position_y + 1][position_x + 1]
            last_row = arr[position_y + 2][position_x:position_x + 3]
            current_sum = sum(first_row) + second_row + sum(last_row)
            maximum_sum = max(current_sum, maximum_sum)
            position_y += 1
        position_x += 1

    return maximum_sum
