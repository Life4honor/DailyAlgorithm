composition = {}

def solution(user_id, banned_id):
    possible_user = {}
    possible_user_cnt = {}
    for banned in banned_id:
        if banned not in possible_user:
            possible_user[banned] = []
        if banned not in possible_user_cnt:
            possible_user_cnt[banned] = 0
        
        possible_user_cnt[banned] += 1
        
        for user in user_id:
            possible = True
            if len(banned) != len(user):
                continue
                
            for idx, char in enumerate(banned):    
                if char == "*":
                    continue
                if char != user[idx]:
                    possible = False
                    break
                    
            if possible and user not in possible_user[banned]:
                possible_user[banned].append(user)
    
    print(possible_user)
    print(possible_user_cnt)
    
    answer = 0
    return answer
    
    
