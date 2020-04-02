# https://leetcode.com/problems/baseball-game/

class Solution:
    def __init__(self):
        self.stack = []

    def calPoints(self, ops: List[str]) -> int:
        result = 0

        for op in ops:
            if op == 'C':
                result -= self.stack.pop()
                continue
            if op == 'D':
                plus = int(self.stack[-1])*2
                self.stack.append(plus)
                result += plus
                continue
            if op == '+':
                plus = sum(self.stack[-2:])
                self.stack.append(plus)
                result += plus
                continue

            self.stack.append(int(op))
            result += int(op)

        return result
