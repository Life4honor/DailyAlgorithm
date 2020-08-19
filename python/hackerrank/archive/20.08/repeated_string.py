# https://www.hackerrank.com/challenges/repeated-string/problem

def repeatedString(s, n):
    result = 0
    length = len(s)

    repeated_times = n // length
    num_of_a = len([char for char in s if char == 'a'])
    result += repeated_times * num_of_a

    lefted_chars_length = n % length
    lefted_chars = s[:lefted_chars_length]
    result += len([char for char in lefted_chars if char == 'a'])

    return result
