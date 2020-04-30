def solution(k, room_number):
    occupied = {}
    answer = []
    for request in room_number:
        if request not in occupied:
            occupied[request] = request + 1
            answer.append(request)
            continue
        
        assigned = occupied[request]
        while assigned in occupied:
            next_ = occupied[assigned]
            occupied[assigned] = occupied[next_] if next_ in occupied else next_
            assigned = next_
        
        occupied[assigned] = assigned + 1
        answer.append(assigned)
    
    return answer
