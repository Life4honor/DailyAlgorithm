# https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    play_count = {}
    play_count_rev = {}
    categorized = {}
    length = len(genres)
    answer = []
    
    for i in range(length):
        genre, count = genres[i], plays[i]
        
        if genre not in categorized:
            categorized[genre] = []
        categorized[genre].append((i, count))
        categorized[genre] = sorted(categorized[genre], reverse=True, key=lambda category:category[1])
        
        if genre not in play_count:
            play_count[genre] = count
            continue
        play_count[genre] += count
    
    for genre, count in play_count.items():
        play_count_rev[count] = genre
    
    for count in sorted(play_count_rev.keys(), reverse=True):
        genre = play_count_rev[count]
        answer += [unique_id for (unique_id, count) in categorized[genre][:2]]
    
    return answer
