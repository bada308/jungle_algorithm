'''
https://www.acmicpc.net/problem/1260
DFS와 BFS

'''

from collections import deque
import sys
input = sys.stdin.readline

n, m, start = map(int, input().split())
path = {}

for _ in range(m):
    a, b = map(int, input().split())
    
    if a in path:
        path[a].append(b)
    else:
        path[a] = [b]
    
    if b in path:
        path[b].append(a)
    else:
        path[b] = [a]

for key in path:
    path[key].sort()

def dfs(path, start):
    result = []
    visited = set()
    stack = [start]
    
    while stack:
        current = stack.pop()
        
        if current not in visited:
            visited.add(current)
            result.append(current)
        
        if current in path:
            for node in reversed(path[current]):
                if node not in visited:
                    stack.append(node)
                    
    return result

def bfs(path, start):
    result = []
    visited = set([start])
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        result.append(current)

        if current in path:
            for node in path[current]:
                if not node in visited:
                    queue.append(node)
                    visited.add(node)
    return result

print(*dfs(path, start), sep=" ")
print(*bfs(path, start), sep=" ")