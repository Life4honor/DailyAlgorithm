# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

def climbingLeaderboard(scores, alice):
    distinct_scores = []
    for score in scores:
        if score not in distinct_scores:
            distinct_scores.append(score)

    result = []
    cache = {}
    for score in alice:
        if score in cache:
            rank = cache[score]
        else:
            rank = find_rank(distinct_scores, score)
            cache[score] = rank
        result.append(rank)

    return result

def find_rank(distinct_scores, score):
    if score in distinct_scores:
        rank = distinct_scores.index(score) + 1
        return rank

    left = 0
    right = len(distinct_scores) - 1
    while True:
        position = (left + right) // 2
        if right - left <= 1:
            if score > distinct_scores[left]:
                return left + 1
            if score > distinct_scores[right]:
                return right +1
            if score < distinct_scores[right]:
                return right + 2

        if score > distinct_scores[position]:
            right = position
        else:
            left = position
