def solution(lines):
    answer = 0
    queue = []
    
    prev_start = None
    for line in lines:
        start, end = convert(line)
        
        time = max(start, prev_start) if prev_start is not None else start
        
        queue.append(end)
        queue = [end for end in queue if time - end < 1.0]
        
        if len(queue) > answer:
            answer = len(queue)
        
        prev_start = start
    return answer

def convert(line):
    hour, minute, sec = line[11:23].split(":")
    duration = line[24:-1]
        
    end = float(hour) * 3600 + float(minute) * 60 + float(sec)
    start = end - float(duration) + 0.001
    return start, end
