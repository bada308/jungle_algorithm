# 2468번 안전 영역 코드 좀 더 깔끔하게

import sys
from collections import deque

input = sys.stdin.readline
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n = int(input())
height_info = [list(map(int, input().split())) for _ in range(n)]
highest = max(max(row) for row in height_info)

def get_safe_area(info, height):
    visited = [[False] * n for _ in range(n)]
    result = 0
    
    for i in range(n):
        for j in range(n):
            if info[i][j] > height and not visited[i][j]:
                queue = deque([(i, j)])
                visited[i][j] = True
                
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in direction:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and info[nx][ny] > height and not visited[nx][ny]:
                            queue.append((nx, ny))
                            visited[nx][ny] = True
                result += 1
    return result

answer = max(get_safe_area(height_info, height) for height in range(1, highest))
print(answer)