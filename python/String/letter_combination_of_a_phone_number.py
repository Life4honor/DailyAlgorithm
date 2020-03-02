# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class LetterTree:
    def __init__(self, digit: str, letter: str):
        self.digit = digit
        self.letter = letter
        self.children = None

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        self.root = LetterTree("", "")
        self.connect_children(self.root, digits)

        self.result = []
        self.combinate(self.root)

        return self.result

    def connect_children(self, node, digits):
        if digits == '':
            return
        digit = digits[0]
        children = []
        for letter in self.letters[digit]:
            child = LetterTree(digit, letter)
            children.append(child)
        node.children = children
        for child in node.children:
            self.connect_children(child, digits[1:])

    def combinate(self, node, result = ""):
        result += node.letter

        if node.children is None:
            if result != "":
                self.result.append(result)
            return

        for child in node.children:
            self.combinate(child, result)

