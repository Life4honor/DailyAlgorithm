# https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        prev = None
        cnt = 1
        size = len(chars)

        for i in range(size):
            char = chars.pop(0)
            if prev == char:
                cnt += 1
            else:
                if cnt > 1:
                    for num in str(cnt):
                        chars.append(num)
                    cnt = 1
                chars.append(char)

            prev = char

            if i == size - 1 and cnt > 1:
                for num in str(cnt):
                    chars.append(num)

        return len(chars)
