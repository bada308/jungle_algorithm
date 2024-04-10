'''
https://www.acmicpc.net/problem/7569
토마토
'''

import sys
from collections import deque
input = sys.stdin.readline
direction = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]



# main
column, row, height = map(int, input().split())
graph = [[] for _ in range(height)]
queue = deque()

for h in range(height):
    for r in range(row):
        tmp = list(map(int, input().split()))
        for c in range(column):
            if tmp[c] == 1:
                queue.append((h, r, c))
        graph[h].append(tmp)
    
while queue:
    ch, cr, cc = queue.popleft()
        
    for dh, dr, dc in direction:
        nh = ch + dh
        nr = cr + dr
        nc = cc + dc
            
        if 0 <= nh < height and 0 <= nr < row and 0 <= nc < column and graph[nh][nr][nc] == 0:
            queue.append((nh, nr, nc))
            graph[nh][nr][nc] = graph[ch][cr][cc] + 1

answer = 0

for h in graph:
    for r in h:
        for c in r:
            if c == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(r))

print(answer-1)