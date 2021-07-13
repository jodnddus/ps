def solution(name):
    min_move = len(name) - 1
    answer = 0

    for i, char in enumerate(name):
        answer += min([ord(char) - 65, abs(ord(char) - 90) + 1])

        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        min_move = min(min_move, i + i + len(name) - next)

    answer += min_move
    return answer 
