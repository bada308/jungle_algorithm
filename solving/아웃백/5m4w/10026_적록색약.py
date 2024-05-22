'''
https://www.acmicpc.net/problem/10026
'''
import sys
from collections import deque
input = sys.stdin.readline

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

n = int(input())
area1 = []
area2 = []
for _ in range(n):
    temp = input().strip()
    area1.append(list(temp))
    area2.append(list(temp.replace("G", "R")))

answer = []


def solve(graph):
    global answer
    visit = set()
    count = 0

    for i in range(n):
        for j in range(n):
            if (i, j) not in visit:
                visit = bfs(graph, visit, i, j)
                count += 1

    answer.append(count)


def bfs(graph, visit, sx, sy):
    q = deque()
    q.append((sx, sy))
    visit.add((sx, sy))
    color = graph[sx][sy]

    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visit and graph[nx][ny] == color:
                visit.add((nx, ny))
                q.append((nx, ny))
    return visit


solve(area1)
solve(area2)

print(*answer)
