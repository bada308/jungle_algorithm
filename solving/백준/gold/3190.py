# https://www.acmicpc.net/problem/3190

from collections import deque
import sys
input = sys.stdin.readline

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

n = int(input())
k = int(input())
apple = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
change = deque([list(input().strip().split()) for _ in range(l)])

queue = deque([(0, 0)])
time = 0
dict_idx = 0

while queue:
    time += 1
    
    x, y = queue[0]
    dx, dy = direction[dict_idx]
    nx, ny = x+dx, y+dy
    
    # 벽이나 본인에 부딪히면 게임 종료
    if nx < 0 or nx >= n:
        break
    if ny < 0 or ny >= n:
        break
    if (nx, ny) in queue:
        break
    
    is_apple = False
    
    # 사과 있는지 확인
    for i in range(len(apple)):
        ax, ay = apple[i]
        if ax-1 == nx and ay-1 == ny:
            is_apple = True
            apple[i] = [-1, -1]
    
    # 사과 없으면 꼬리 빼기
    if not is_apple:
        queue.pop()
    
    # 머리 넣기
    queue.appendleft((nx, ny))
    
    
    # 방향 전환
    if len(change) > 0 and int(change[0][0]) == time:
        if change[0][1] == "L":
            dict_idx -= 1
            if dict_idx < 0:
                dict_idx = 3
        else:
            dict_idx += 1
            if dict_idx > 3:
                dict_idx = 0
        change.popleft()

print(time)