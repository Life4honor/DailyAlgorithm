def solution(record):
    queue = []
    user_nick = {}
    action_msg = {
        'Enter': '들어왔습니다.',
        'Leave': '나갔습니다.',
    }

    for rec in record:
        action, id_, nickname = None, None, None
        splited = rec.split(" ")
        if len(splited) == 2:
            action, id_ = splited

        if len(splited) == 3:
            action, id_, nickname = splited

        if action != "Leave":
            user_nick[id_] = nickname

        if action == "Change":
            continue
        queue.append((id_, action))

    answer = [f"{user_nick[id_]}님이 {action_msg[action]}" for id_, action in queue]
    return answer
