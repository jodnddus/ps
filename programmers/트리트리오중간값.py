# https://programmers.co.kr/learn/courses/30/lessons/68937?language=python3
# https://prgms.tistory.com/32?category=882795
from test import check_test_case
from collections import deque

def BFS(graph, start):
    dist = []
    queue = deque([[start, 0]])
    visit = {start: True}

    while queue:
        cur_node, cur_dist = queue.popleft()
        dist.append([cur_node, cur_dist])

        for val in graph[cur_node]:
            if val not in visit:
                queue.append([val, cur_dist + 1])
                visit[val] = True

    return dist

def solution(n, edges):
    graph = {i + 1: [] for i in range(n)}
    for cur in edges:
        graph[cur[0]].append(cur[1])
        graph[cur[1]].append(cur[0])

    #1 임의의 정점에서 가장 가까운 순서대로 정점들을 구한다
    start = BFS(graph, 1)
    #2 #1에서 구한 정점들에서 가장 먼 정점을 구한다
    end = BFS(graph, start[-1][0])

    #3 #1에서 구한 정점들 중 가장 먼 순서대로 2개를 가져온다
    check1, check2 = start[-2][1], start[-1][1]

    #4 혹시 #1에서 구한 정점 두개가 같은 거리에 있다면 지름이 두개 있다는 의미
    if check1 == check2: return end[-1][1]
    #5 그게 아니라면 중간값인 마지막에서 두번째 정점의 거리를 리턴
    else: return end[-2][1]


check_test_case(solution(4, [[1, 2], [2, 3], [3, 4]]), 2)
check_test_case(solution(5, [[1, 5], [2, 5], [3, 5], [4, 5]]), 2)
