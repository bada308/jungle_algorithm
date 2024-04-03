'''
https://www.acmicpc.net/problem/1707
이분 그래프
'''

from collections import deque
import sys
input = sys.stdin.readline


k = int(input())

def bfs(start, setA, setB, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        current = queue.popleft()
        if current in setA:
            ver = "B"
        else:
            ver = "A"
        for node in edges[current]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)
                if ver == "A":
                    if all(v not in setA for v in edges[node]):
                        setA.add(node)
                    else:
                        return False
                else:
                    if all(v not in setB for v in edges[node]):
                        setB.add(node)
                    else:
                        return False
    
    return True

for _ in range(k):
    v, e = map(int, input().split())
    
    edges = [[] for _ in range(v)]
    
    for _ in range(e):
        a, b = map(int, input().split())
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)
    
    setA = set([0])
    setB = set()
    visited = [False for _ in range(v)]
    
    result = []
    
    while True:
        if all(visit == True for visit in visited):
            break
        for i in range(v):
            if visited[i] == False:
                result.append(bfs(i, setA, setB, visited))
                continue
    if all(result):
        print("YES")
    else:
        print("NO")