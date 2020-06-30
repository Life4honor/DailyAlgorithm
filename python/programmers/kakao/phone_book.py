# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    samples = [phone for phone in phone_book]
    for phone in phone_book:
        for sample in samples:
            if sample == phone:
                continue
            if sample == phone[:len(sample)]:
                return False
    return True
