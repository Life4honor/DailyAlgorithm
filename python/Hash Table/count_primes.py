# https://leetcode.com/problems/count-primes/

class Solution:
    def __init__(self):
        self.prime_numbers = [2]

    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        for number in range(3, n):
            if self.is_prime(number):
                self.prime_numbers.append(number)

        return len(self.prime_numbers)

    def is_prime(self, number):
        for prime_number in self.prime_numbers:
            if number % prime_number == 0:
                return False
        return True
