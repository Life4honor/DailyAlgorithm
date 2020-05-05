def solution(board, moves):
    answer = 0
    basket = []
    columns = {}
    
    for i in range(len(board)):
        column = [row[i] for row in board if row[i] != 0]
        columns[i+1] = column
    
    for move in moves:
        if columns[move] == []:
            continue
        popped = columns[move].pop(0)
        if basket != [] and basket[-1] == popped:
            answer += 2
            basket.pop()
            continue
        basket.append(popped)
    
    return answer
