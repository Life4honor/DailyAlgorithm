# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_in_a_line = []
        for row in board:
            board_in_a_line += row

        row_idx = 0
        column_idx = 0
        box_idx = 0

        rows = []
        while row_idx < 9:
            row = []
            start_idx = 9 * row_idx
            for i in range(start_idx, start_idx + 9):
                row.append(board_in_a_line[i])

            rows.append(row)
            row_idx += 1

        columns = []
        while column_idx < 9:
            temp = [0,1,2,3,4,5,6,7,8]
            column = []

            targets = [9*el + column_idx for el in temp]
            for i in targets:
                column.append(board_in_a_line[i])

            columns.append(column)
            column_idx += 1


        sub_boxes = []
        temp = [0,1,2,9,10,11,18,19,20]
        start_idx = [0, 3, 6, 27, 30, 33, 54, 57, 60]
        targets = []
        sub_box = []
        for i in start_idx:
            targets = [digit + i for digit in temp]
            for target in targets:
                sub_box.append(board_in_a_line[target])

            sub_boxes.append(sub_box)
            sub_box = []

        return self.is_valid(rows) and self.is_valid(columns) and self.is_valid(sub_boxes)


    def is_valid(self, elements):

        for element in elements:
            cache = []
            for digit in element:
                if digit == '.':
                    continue

                if digit in cache:
                    return False
                cache.append(digit)

        return True
