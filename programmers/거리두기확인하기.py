# https://programmers.co.kr/learn/courses/30/lessons/81302
# https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-%EA%B1%B0%EB%A6%AC%EB%91%90%EA%B8%B0-%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0-Python
# bfs
from test import check_test_case
from collections import deque


def bfs(place):
    p_nodes = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for y in range(5):
        for x in range(5):
            if place[y][x] == "P":
                p_nodes.append([y, x])

    for p in p_nodes:
        visited = [[0] * 5 for _ in range(5)]
        distance = [[0] * 5 for _ in range(5)]
        q = deque([p])

        visited[p[0]][p[1]] = 1

        while q:
            y, x = q.popleft()

            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]

                if 0 <= new_x < 5 and 0 <= new_y < 5 and not visited[new_y][new_x]:
                    visited[new_y][new_x] = 1

                    if place[new_y][new_x] == "O":
                        q.append([new_y, new_x])
                        visited[new_y][new_x] = 1
                        distance[new_y][new_x] = distance[y][x] + 1

                    if place[new_y][new_x] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []

    for place in places:
        answer.append(bfs(place))

    return answer


check_test_case(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], [
                "PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]), [1, 0, 1, 1, 1])
