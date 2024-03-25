# https://www.acmicpc.net/problem/2468

import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n = int(input())
height_info = [list(map(int, input().split())) for _ in range(n)]

highest = 0

for i in height_info:
    max_tmp = max(i)
    if max_tmp > highest:
        highest = max_tmp

answer = 0

def get_safe_area(info):
    result = 0
    for i in range(n):
        for j in range(n):
            if info[i][j]:
                queue = deque()
                queue.append((i, j))
                while queue:
                    (x, y) = queue.popleft()
                    for k in range(4):
                        next_x = x + direction[k][0]
                        next_y = y + direction[k][1]
                        
                        if 0 <= next_x < n and 0 <= next_y < n and info[next_x][next_y]:
                            queue.append((next_x, next_y))
                            info[next_x][next_y] = False
                result += 1
                info[i][j] = False
    return result

for i in range(highest):
    tmp_info = deepcopy(height_info)
    
    for x in range(n):
        for y in range(n):
            if tmp_info[x][y] > i:
                tmp_info[x][y] = True
            else:
                tmp_info[x][y] = False
    answer = max(answer, get_safe_area(tmp_info))

print(answer)