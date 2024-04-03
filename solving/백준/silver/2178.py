'''
https://www.acmicpc.net/problem/2178
미로 탐색
'''

import sys
from collections import deque
input = sys.stdin.readline
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs():
    shortest = int(1e8)
    visited = set([(0, 0)])
    queue = deque([(0, 0, 1)])
    
    
    while queue:
        x, y, cost = queue.popleft()
        
        if x == n - 1 and y == m - 1:
            shortest = min(cost, shortest)
            continue
        
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] and (nx, ny) not in visited:
                queue.append((nx, ny, cost + 1))
                visited.add((nx, ny))

    return shortest

# main
n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

print(bfs())

