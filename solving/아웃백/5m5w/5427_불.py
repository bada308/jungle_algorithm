'''
https://www.acmicpc.net/problem/5427
'''
import sys
from collections import deque
input = sys.stdin.readline

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def solve(graph):
    fire_queue = deque([])
    sang_queue = deque([])
    visit = set()
    for i in range(h):
        for j in range(w):
            if graph[i][j] == "*":
                graph[i][j] = 0
                fire_queue.append((i, j, 0))
            if graph[i][j] == "@":
                sang_queue.append((i, j, 0))

    # 불 번진 time으로 graph 갱신
    while fire_queue:
        fh, fw, ftime = fire_queue.popleft()
        for dh, dw in direction:
            nh, nw = fh + dh, fw + dw
            if 0 <= nh < h and 0 <= nw < w and (graph[nh][nw] == "." or graph[nh][nw] == "@"):
                graph[nh][nw] = ftime + 1
                fire_queue.append((nh, nw, ftime + 1))

    # 상근이가 움직일 수 있을 때까지 반복
    while sang_queue:
        sh, sw, time = sang_queue.popleft()
        visit.add((sh, sw))
        for dh, dw in direction:
            nh, nw = sh + dh, sw + dw

            # 탈출 성공 시 return
            if not 0 <= nh < h or not 0 <= nw < w:
                return time + 1

            # 이동 가능한 곳이 있을 시 queue에 push
            if graph[nh][nw] != "#" and (nh, nw) not in visit and (graph[nh][nw] == "." or graph[nh][nw] > time + 1):
                sang_queue.append((nh, nw, time + 1))
                visit.add((nh, nw))

    return "IMPOSSIBLE"


# main

# input
t = int(input())
answer = []

for __ in range(t):
    w, h = map(int, input().split())
    answer.append(solve([list(input().strip()) for __ in range(h)]))

print(*answer, sep="\n")
