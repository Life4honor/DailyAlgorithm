# https://leetcode.com/problems/complex-number-multiplication/

class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        real_a, imaginary_a = a.split('+')
        real_b, imaginary_b = b.split('+')

        real_int_a = int(real_a)
        real_int_b = int(real_b)
        imaginary_int_a = int(imaginary_a[:-1])
        imaginary_int_b = int(imaginary_b[:-1])
        real_part = real_int_a * real_int_b - imaginary_int_a * imaginary_int_b
        imaginary_part = real_int_a * imaginary_int_b + real_int_b * imaginary_int_a
        result = str(real_part) + "+" + str(imaginary_part) + "i"
        return result

