# https://programmers.co.kr/learn/courses/30/lessons/42626

def recurse(scoville, K, answer):
    if len(scoville) == 2 and scoville[0] < K:
        return -1 if scoville[0] + scoville[1]*2 < K else answer + 1
    
    first_place = scoville.pop(0)
    if first_place >= K:
        return answer
    
    second_place = scoville.pop(0)
    
    new_one = first_place + second_place*2
    scoville.append(new_one)
    scoville = sorted(scoville)
    answer += 1
    return recurse(scoville, K, answer)

def solution(scoville, K):
    answer = 0
    return recurse(scoville, K, answer) if K > 0 else answer
