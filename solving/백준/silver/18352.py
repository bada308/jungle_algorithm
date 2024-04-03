'''
https://www.acmicpc.net/problem/18352
특정 거리의 도시 찾기

다익스트라 문제!
'''

import heapq
import sys
input = sys.stdin.readline
INF = int(1e8)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def dijkstra(start):
    min_heap = []
    
    distance[start] = 0
    visited[start] = False
    
    for node in graph[start]:
        distance[node] = distance[start] + 1
        heapq.heappush(min_heap, (distance[node], node))
    
    while min_heap:
        current = heapq.heappop(min_heap)
        
        for node in graph[current[1]]:
            if distance[node] > distance[current[1]] + 1:
                distance[node] = distance[current[1]] + 1
                heapq.heappush(min_heap, (distance[node], node))

dijkstra(x)

answer = []

for i in range(1, n+1):
    if distance[i] == k:
        answer.append(i)
if not answer: print(-1)
else: print(*answer, sep="\n")