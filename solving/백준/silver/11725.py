'''
https://www.acmicpc.net/problem/11725
트리의 부모 찾기
'''

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

edges = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    
    edges[a].append(b)
    edges[b].append(a)

parent = [-1 for _ in range(n+1)]

def bfs(start):
    visited = set([start])
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        
        for node in edges[current]:
            if node not in visited:
                parent[node] = current
                visited.add(node)
                queue.append(node)

bfs(1)

print(*parent[2:], sep="\n")