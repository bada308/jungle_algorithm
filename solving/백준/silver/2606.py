'''
https://www.acmicpc.net/problem/2606
바이러스
'''

from collections import deque
import sys
input = sys.stdin.readline

v = int(input())
e = int(input())

edges = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)


def bfs(start):
    count = 0
    visited = set([start])
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        
        for node in edges[current]:
            if node not in visited:
                visited.add(node)
                queue.append(node)
                count += 1
    return count

print(bfs(1))