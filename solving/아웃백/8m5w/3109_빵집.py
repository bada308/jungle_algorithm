'''
https://www.acmicpc.net/problem/3109
'''
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
map = [list(input().strip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]

def dfs(x, y):
    visited[x][y] = True
    if y == c - 1:
        return True
    for dx in [-1, 0, 1]: # 오른쪽 위를 먼저 탐색 (그리디)
        cx, cy = x + dx, y + 1
        if 0 <= cx < r and map[cx][cy] == '.' and not visited[cx][cy]:
            if dfs(cx, cy):
                return True
    return False

answer = 0
for i in range(r):
    if dfs(i, 0):
        answer += 1

print(answer)