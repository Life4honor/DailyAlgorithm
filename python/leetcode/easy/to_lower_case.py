# https://leetcode.com/problems/to-lower-case/

class Solution:
    def toLowerCase(self, str_: str) -> str:
        uppercasemap = {
            'A': 'a',
            'B': 'b',
            'C': 'c',
            'D': 'd',
            'E': 'e',
            'F': 'f',
            'G': 'g',
            'H': 'h',
            'I': 'i',
            'J': 'j',
            'K': 'k',
            'L': 'l',
            'M': 'm',
            'N': 'n',
            'O': 'o',
            'P': 'p',
            'Q': 'q',
            'R': 'r',
            'S': 's',
            'T': 't',
            'U': 'u',
            'V': 'v',
            'W': 'w',
            'X': 'x',
            'Y': 'y',
            'Z': 'z'
        }

        result = ""

        for char in str_:
            if char in uppercasemap:
                char = uppercasemap[char]
            result += char

        return result

