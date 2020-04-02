# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s

        length = len(s)
        num_columns = 0

        while length > 0:
            num_columns += 1
            length = length - num_rows if num_columns % num_rows == 0 else length - 1

        result = [copy.deepcopy([""]*num_rows) for i in range(num_columns)]

        position_x, position_y = 0,0

        idx = 0

        while idx <= len(s) - 1:
            while position_y < num_rows - 1:
                if idx == len(s):
                    break

                result[position_x][position_y] = s[idx]
                idx += 1
                position_y += 1

            while position_y > 0 and position_x < num_columns:
                if idx == len(s):
                    break
                result[position_x][position_y] = s[idx]
                position_x += 1
                position_y -= 1
                idx += 1

        output = ''
        for row_idx in range(num_rows):
            for column_idx in range(num_columns):
                if result[column_idx][row_idx] != '':
                    output += result[column_idx][row_idx]

        return output

