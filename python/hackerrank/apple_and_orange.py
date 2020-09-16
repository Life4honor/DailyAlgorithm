# https://www.hackerrank.com/challenges/apple-and-orange/problem

from collections import defaultdict

def countApplesAndOranges(s, t, a, b, apples, oranges):
    house_range = defaultdict(bool)
    for i in range(s, t+1):
        house_range[i] = True

    apple_locations =[a + apple for apple in apples]
    orange_locations = [b + orange for orange in oranges]

    apple_count = len([apple for apple in apple_locations if house_range[apple]])
    orange_count = len([orange for orange in orange_locations if house_range[orange]])

    print(apple_count)
    print(orange_count)
