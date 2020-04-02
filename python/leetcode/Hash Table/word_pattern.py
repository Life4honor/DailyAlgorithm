# https://leetcode.com/problems/word-pattern/

class Solution:
    def __init__(self):
        self.dict = {}
        self.cache = []

    def wordPattern(self, pattern: str, str_input: str) -> bool:
        splited = str_input.split(" ")

        if len(pattern) != len(splited):
            return False

        for idx, char in enumerate(pattern):
            if char not in self.dict:
                self.dict[char] = []
            self.dict[char].append(idx)

        for same_pattern_idx_group in [self.dict[key] for key in self.dict]:
            expected_pattern = None
            for idx in same_pattern_idx_group:
                if expected_pattern == None:
                    expected_pattern = splited[idx]
                    if expected_pattern in self.cache:
                        return False
                    self.cache.append(expected_pattern)

                if splited[idx] != expected_pattern:
                    return False

        return True
