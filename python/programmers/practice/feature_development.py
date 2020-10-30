# https://programmers.co.kr/learn/courses/30/lessons/42586

def recurse(progresses, speeds, times, deploy, answer):
    if progresses == [] or speeds == []:
        return list(answer.values())
    
    speed = speeds[0]
    progress = progresses[0]
    
    if progress + speed * times >= 100:
        if times not in answer:
            answer[times] = 0
        
        answer[times] += 1
        progresses = progresses[1:]
        speeds = speeds[1:]
        
        deploy += 1
        return recurse(progresses, speeds, times, deploy, answer)
    
    times += 1
    deploy = 0
    return recurse(progresses, speeds, times, deploy, answer)
    

def solution(progresses, speeds):
    return recurse(progresses, speeds, 0, 0, {})
