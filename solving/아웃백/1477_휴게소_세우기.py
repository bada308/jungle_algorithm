'''
https://www.acmicpc.net/problem/1477
'''
import sys
import heapq

input = sys.stdin.readline

n, m, l = map(int, input().split())
locations = [0] + list(map(int, input().split())) + [l]
locations.sort()

max_heap = []
for i in range(1, len(locations)):
    heapq.heappush(max_heap, -1 * (locations[i] - locations[i-1]))

print(locations, max_heap)

for _ in range(m):
    top = heapq.heappop(max_heap) * -1
    heapq.heappush(max_heap, -1 * ((top + 1) // 2))
    print(max_heap)

print(heapq.heappop(max_heap) * -1)
