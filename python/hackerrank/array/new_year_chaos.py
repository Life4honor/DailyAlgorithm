# https://www.hackerrank.com/challenges/new-year-chaos/problem

def minimumBribes(q):

    if is_chaotic(q):
        print("Too chaotic")
        return

    initial_position = sorted(q)
    bribe_count = 0
    offset = 0

    while q[offset] == offset+1:
        offset += 1

    while q != initial_position:
        offset += 1 if q[offset] == offset+1 else 0
        unsorted_part = q[offset:]

        for idx, _ in enumerate(unsorted_part):
            if unsorted_part[idx] > unsorted_part[idx+1]:
                q[offset+idx], q[offset+idx+1] = q[offset+idx+1], q[offset+idx]
                bribe_count += 1
                break

    print(bribe_count)

def is_chaotic(q):
    for idx, sticker in enumerate(q):
        position = idx + 1
        if sticker - position > 2:
            return True
    return False
