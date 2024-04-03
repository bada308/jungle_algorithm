'''
https://www.acmicpc.net/problem/21606
아침 산책
'''
from collections import deque
import sys
input = sys.stdin.readline


# 함수 영역
def get_path(start):
    visit[start] = True
    queue = deque([start])
    count = 0
    
    while queue:
        current = queue.popleft()
        for next in graph[current]:
            if infos[next]: # 실내이면
                count += 1
            elif not infos[next] and not visit[next]:
                queue.append(next)
                visit[next] = True
    return count

# main
n = int(input())
infos = [0] + list(map(int, input().strip()))
graph = [[] for _ in range(n+1)]
answer = 0
visit = [False for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    if not infos[a]:
        graph[a].append(b)
    if not infos[b]:
        graph[b].append(a)
    if infos[a] and infos[b]:
        answer += 2

for i in range(1, n+1):
    if not infos[i] and not visit[i]:
        result = get_path(i)
        answer += result * (result - 1)

print(answer)