'''
https://www.acmicpc.net/problem/1103
x -> n / y -> m
'''
### BFS 도전 -> 사이클 판별이 어려움 ###
# from collections import deque
# import sys
# input = sys.stdin.readline

# direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# hole = 0

# n, m = map(int, input().split())
# board = [list(map(int, list(input().strip().replace('H', str(hole))))) for __ in range(n)]
# result = [[0] * m for __ in range(n)]

# result[0][0] = 1
# queue = deque([(0, 0)])

# while queue:
#     x, y = queue.popleft()
#     num = board[x][y]
#     for dx, dy in direction:
#         nx, ny = x + dx * num, y + dy * num
#         if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != hole:
#             if 0 < result[nx][ny] < result[x][y]: # 사이클 판단을 이상하게 하고 있음
#                 print(-1)
#                 exit(0)
#             result[nx][ny] = result[x][y] + 1
#             queue.append((nx, ny))

# answer = 1
# for r in result:
#     answer = max(answer, max(r))
# print(answer)

### DFS로 도전 ###
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
hole = 0

n, m = map(int, input().split())
board = [list(map(int, list(input().strip().replace('H', str(hole))))) for __ in range(n)]
dp = [[-1] * m for __ in range(n)]
visited = [[False] * m for __ in range(n)]

def dfs(x, y):
    if visited[x][y]:
        print(-1)
        sys.exit(0)
    if dp[x][y] != -1:
        return dp[x][y]
    
    visited[x][y] = True
    max_moves = 1
    for dx, dy in direction:
        nx, ny = x + board[x][y] * dx, y + board[x][y] * dy
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != hole:
            max_moves = max(max_moves, dfs(nx, ny) + 1)
    visited[x][y] = False
    dp[x][y] = max_moves
    return dp[x][y]

answer = dfs(0, 0)
print(answer)