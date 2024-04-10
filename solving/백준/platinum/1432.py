'''
https://www.acmicpc.net/problem/1432
그래프 수정
'''

import sys
import heapq
input = sys.stdin.readline

n = int(input())

outdegree = [0 for _ in range(n)]
graph = [[] for _ in range(n)]

# 입력 받으면서 진출 차수 계산
for x in range(n):
    tmp = list(map(int, input().strip()))
    for y in range(n):
        if tmp[y]:
            outdegree[x] += 1
            graph[y].append(x)


heap = []                     # 인덱스가 가장 높은 곳부터 처리하기 위한 최대 힙
change= [0 for _ in range(n)] # 수정 결과를 저장하는 배열
MAX = n                       # 처리 시점에 가장 큰 수를 저장하는 변수

# 진출차수 0인 노드 최대 힙에 저장
for i in range(n):
    if outdegree[i] == 0:
        heapq.heappush(heap, -1 * i)

# 힙이 빌 때까지 그래프 수정 처리
while heap:
    current = heapq.heappop(heap) * -1
    change[current] = MAX
    MAX -= 1
    
    for next in graph[current]:
        outdegree[next] -= 1
        if outdegree[next] == 0:
            heapq.heappush(heap, -1 * next)

# 모든 노드가 수정 처리 됐으면 사이클 존재 X
if all(change):
    print(*change)
else:
    print(-1)