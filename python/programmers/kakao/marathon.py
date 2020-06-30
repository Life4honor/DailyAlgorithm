# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    participant_cnt = {}
    for athelete in participant:
        if athelete not in participant_cnt:
            participant_cnt[athelete] = 0
        participant_cnt[athelete] += 1
        
    for winner in completion:
        participant_cnt[winner] -= 1
    
    answer = [name for name in participant_cnt if participant_cnt[name] == 1][0]
    return answer
