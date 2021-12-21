def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    counts = [0, 0, 0]

    for index, answer in enumerate(answers):
        if answer == a[index % len(a)]:
            counts[0] += 1
        if answer == b[index % len(b)]:
            counts[1] += 1
        if answer == c[index % len(c)]:
            counts[2] += 1

    answer = [i + 1 for i, value in enumerate(counts) if value == max(counts)]
    return answer


solution([1, 2, 3, 4, 5])
solution([1, 3, 2, 4, 2])
