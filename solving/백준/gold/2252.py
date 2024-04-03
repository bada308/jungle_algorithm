'''
https://www.acmicpc.net/problem/2252
줄 세우기

완전 위상정렬 그 자체!
'''
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topological_sort():
    queue = deque()
    result = []
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        current = queue.popleft()
        result.append(current)
        
        for node in graph[current]:
            indegree[node] -= 1
            if indegree[node] == 0: queue.append(node)
    
    return result

print(*topological_sort())