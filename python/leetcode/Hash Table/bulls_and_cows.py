# https://leetcode.com/problems/bulls-and-cows/

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count_bulls = 0
        count_cows = 0
        count_popped = 0
        original = secret
        left = []
        
        
        for idx, num in enumerate(guess):
            if num == original[idx]:
                secret = secret[:idx-count_popped] + secret[idx-count_popped+1:]
                count_popped += 1
                count_bulls += 1
                continue
            
            left.append(num)
        
        for num in left:
            if num in secret:
                count_cows += 1
                idx = secret.index(num)
                secret = secret[:idx] + secret[idx+1:]
            
        return f'{count_bulls}A{count_cows}B'
