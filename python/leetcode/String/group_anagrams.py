# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_by_component = {}
        cache = []
        for word in strs:
            sorted_chars = sorted(word)
            sorted_word = ""
            for char in sorted_chars:
                sorted_word += char

            if sorted_word not in cache:
                cache.append(sorted_word)
                grouped_by_component[sorted_word] = []

            grouped_by_component[sorted_word].append(word)

        return [grouped_by_component[key] for key in grouped_by_component]

