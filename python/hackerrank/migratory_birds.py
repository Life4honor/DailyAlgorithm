# https://www.hackerrank.com/challenges/migratory-birds/problem

def migratoryBirds(arr):
    types = {1:0, 2:0, 3:0, 4:0, 5:0}
    for el in arr:
        types[el] += 1

    result = 1
    for type_, count in types.items():
        if types[result] == count and type_ > result:
            continue
        
        if types[result] < count:
            result = type_
            
    return result