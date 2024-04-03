'''
https://www.acmicpc.net/problem/11724
연결 요소의 개수
'''

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    edges[u-1].append(v-1)
    edges[v-1].append(u-1)

visited = [False] * n
answer = 0

def bfs(start):
    global visited, answer
    answer += 1
    queue = deque([start])
    visited[start] = True
    
    while queue:
        current = queue.popleft()
        
        for node in edges[current]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)

while True:
    if all(visit == True for visit in visited):
        break
    
    for i in range(n):
        if visited[i] == False:
            bfs(i)
            continue

print(answer)