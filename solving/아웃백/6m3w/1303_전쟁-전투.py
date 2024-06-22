'''
https://www.acmicpc.net/problem/1303
'''
import sys
from collections import deque
input = sys.stdin.readline
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(pos, team):
    count = 0
    queue = deque([pos])
    visited[pos[0]][pos[1]] = True
    while queue:
        x, y = queue.popleft()
        count += 1
        for dx, dy in direction:
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == team:
                queue.append((nx, ny))
                visited[nx][ny] = True
    return count


n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(m)]
visited = [[False]*n for __ in range(m)]
score = {"W": 0, "B": 0}

for i in range(m):
    for j in range(n):
        if visited[i][j]:
            continue
        score[graph[i][j]] += (bfs((i, j), graph[i][j]) ** 2)

print(*list(score.values()), sep=" ")
