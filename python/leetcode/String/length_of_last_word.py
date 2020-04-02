# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splited = s.split(" ")
        last_word = splited.pop()
        while last_word == '':
            if splited == []: break
            last_word = splited.pop()
        return len(last_word)
