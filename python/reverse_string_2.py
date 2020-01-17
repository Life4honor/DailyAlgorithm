# https://leetcode.com/problems/reverse-string-ii/

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""

        do_reverse = True

        while len(s) >= 2*k:
            substring = s[:2*k]
            result += self.partial_reverse(substring, k)
            s = s[2*k:]

        if len(s) > k:
            result += self.partial_reverse(s, k)
        else:
            result += s[::-1]

        return result

    def partial_reverse(self, s: str, k: int):
        pref_substring = s[:k][::-1]
        suf_substring = s[k:]
        return pref_substring + suf_substring

