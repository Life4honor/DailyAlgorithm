# https://www.hackerrank.com/challenges/ctci-ransom-note/problem

def checkMagazine(magazine, note):
    count_word = {}
    for word in magazine:
        count_word[word] = 1 if word not in count_word else count_word[word] + 1

    for word in note:
        if word not in count_word:
            print("No")
            return

        count_word[word] -= 1
        if count_word[word] < 0:
            print("No")
            return

    print("Yes")
    return
