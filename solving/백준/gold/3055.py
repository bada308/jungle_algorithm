'''
https://www.acmicpc.net/problem/3055
탈출
'''

import sys
from collections import deque
input = sys.stdin.readline
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

row, column = map(int, input().split())
table = []

start = None
water = []


for r in range(row):
    tmp = list(input().strip())
    for c in range(column):
        if tmp[c] == "*":
            water.append((r, c, 0))
        if tmp[c] == "S":
            start = (r, c)
    table.append(tmp)

def flow():
    visit = [[False]*column for _ in range(row)]
    queue = deque(water)
    for a, b, _ in water:
        visit[a][b] = True
    
    while queue:
        x, y, count = queue.popleft()
        table[x][y] = count
        
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < row and 0 <= ny < column and not visit[nx][ny]:
                visit[nx][ny] = True
                if table[nx][ny] == "X" or table[nx][ny] == "D" or table[nx][ny] == "S":
                    continue
                queue.append((nx, ny, count + 1))


def move():
    visit = [[False]*column for _ in range(row)]
    queue = deque([(start[0], start[1], 0)])
    visit[start[0]][start[1]] = True
    
    while queue:
        x, y, count = queue.popleft()
        
        if table[x][y] == "D":
            return count
        
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < row and 0 <= ny < column and not visit[nx][ny]:
                visit[nx][ny] = True
                if type(table[nx][ny]) is int and table[nx][ny] <= count + 1:
                    continue
                if table[nx][ny] == "X":
                    continue
                queue.append((nx, ny, count + 1))
    return "KAKTUS"

flow()

print(move())