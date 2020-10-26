# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

def breakingRecords(scores):
    max_score, min_score = None, None

    max_break_count, min_break_count = 0,0

    for score in scores:
        if max_score is None:
            max_score = score

        if min_score is None:
            min_score = score
        
        if score > max_score:
            max_score = score
            max_record_count += 1

        if score < min_score:
            min_score = score
            min_record_count += 1        

    return max_break_count, min_break_count
