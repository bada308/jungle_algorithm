'''
https://www.acmicpc.net/problem/15903

아기 석환이

x번 y번 카드를 골라서 두 카드의 value를 value[x]+value[y]로 덮어씌우는 게임
m번 합체를 하고난 후, 모든 카드의 value의 합이 `최소`가 되어야 함.

그리디......???? 인가
정렬 사용 시 200ms -> 우선순위 큐 사용 시 48ms
'''
# 정렬 사용
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# values = list(map(int, input().split()))

# for _ in range(m):
#     values.sort()
#     values[0], values[1] = values[0] + values[1], values[0] + values[1]

# print(sum(values))

# 우선순위 큐 사용
import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
values = list(map(int, input().split()))
heapq.heapify(values)

for _ in range(m):
    a = heapq.heappop(values)
    b = heapq.heappop(values)
    
    heapq.heappush(values, a + b)
    heapq.heappush(values, a + b)

print(sum(values))