'''
https://www.acmicpc.net/problem/2573
'''
import sys
from collections import deque
input = sys.stdin.readline

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(visit, ice):
    global graph
    melted = set()
    queue = deque()
    init = list(ice)[0]
    queue.append(init)
    visit.add((init[0], init[1]))

    while queue:
        x, y = queue.popleft()
        sea = 0
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if (0 <= nx < n and 0 <= ny < m and (nx, ny) not in visit):
                if graph[nx][ny] == 0:
                    sea += 1
                else:
                    queue.append((nx, ny))
                    visit.add((nx, ny))
        melted.add((x, y, sea))

    for x, y, sea in list(melted):
        graph[x][y] = max(0, graph[x][y] - sea)
        if graph[x][y] == 0:
            ice.remove((x, y))


n, m = map(int, input().split())

graph = []
ice = set()


for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)
    for j in range(m):
        if temp[j]:
            ice.add((i, j))


answer = 0
year = 0

while ice:
    visit = set()
    bfs(visit, ice)
    if (ice - visit):
        answer = year
        break
    year += 1


print(answer)
