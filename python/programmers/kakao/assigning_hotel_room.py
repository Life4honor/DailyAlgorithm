def solution(k, room_number):
    occupied_rooms = {}
    answer = []
    for room in room_number:
        if room not in occupied_rooms:
            occupied_rooms[room] = True
            answer.append(room)
            continue

        room_no = room
        while room_no in occupied_rooms:
            room_no += 1
        occupied_rooms[room_no] = True
        answer.append(room_no)

    return answer
