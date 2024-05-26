'''
https://www.acmicpc.net/problem/15686

치킨 거리: 집과 가장 가까운 치킨집 사이의 거리
- 집을 기준으로 정해짐

도시의 치킨 거리: 모든 집의 치킨 거리의 합

치킨집을 M개만 남겨놓고 모두 폐업해야 한다.
목표 : 도시의 치킨 거리가 가장 작게 되도록 치킨집 폐업

치킨 to 집 로 구함

치킨 거리 테이블
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
house = []
chicken_place = []


for i in range(n):
    temp_list = list(map(int, input().split()))
    for j in range(n):
        if temp_list[j] == 1:
            house.append((i, j))
        if temp_list[j] == 2:
            chicken_place.append((i, j))

nearest_count = [[0, i] for i in range(len(chicken_place))]

for hx, hy in house:
    for k in range(len(chicken_place)):
        cx, cy = chicken_place[k]
        nearest_count[k][0] += (abs(hx - cx) + abs(hy - cy))


nearest_count.sort()
nearest_count = nearest_count[:m]


answer = 0
for hx, hy in house:
    distance = int(1e8)
    for _, idx in nearest_count:
        cx, cy = chicken_place[idx]
        if abs(hx - cx) + abs(hy - cy) < distance:
            distance = abs(hx - cx) + abs(hy - cy)
    answer += distance
print(answer)
