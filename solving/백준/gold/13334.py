# https://www.acmicpc.net/problem/13334

import sys
import heapq
input = sys.stdin.readline

n = int(input())

datas = [list(map(int, input().split())) for _ in range(n)]
d = int(input())
roads = []

for data in datas:
    h, o = data
    
    if abs(h - o) <= d:
        roads.append((min(h, o), max(h, o)))

roads.sort(key=lambda x: x[1])

min_heap = []
answer = 0

for road in roads:
    start = road[1] - d
    heapq.heappush(min_heap, road)
    while min_heap and min_heap[0][0] < start:
        heapq.heappop(min_heap)
    answer = max(answer, len(min_heap))

print(answer)