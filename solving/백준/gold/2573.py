'''
https://www.acmicpc.net/problem/2573
빙산
'''

import sys
from collections import deque
input = sys.stdin.readline
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(sx, sy):
    visit[sx][sy] = True
    queue = deque([(sx, sy)])
    sea_list = []
    
    while queue:
        sea = 0
        x, y = queue.popleft()
        
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] and (nx, ny) not in visit[nx][ny]:
                    queue.append((nx, ny))
                    sea += 1
        
        if sea > 0:
            sea_list.append((x, y, sea))
    
    for x, y, sea in sea_list:
        graph[x][y] = max(0, graph[x][y] - sea)


year = 0
while ice:
    visit = [[False] * m for _ in range(n)]
    group = 0
    
    for i in range(n):
        for j in range(m):
            if not visit[i][j]:
                group += bfs(i, j)
    
    if group >= 2:
        break
    
    