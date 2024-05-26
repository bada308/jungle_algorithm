'''
https://www.acmicpc.net/problem/15686
'''
import sys
from itertools import combinations
input = sys.stdin.readline


# Data structure
house = []  # 집의 위치를 저장하는 배열
chicken = []  # 치킨 가게의 위치를 저장하는 배열


# Utils
def get_chicken_distance(house_position, chicken_list):
    """
    집과 가장 가까운 치킨집 사이의 거리를 구한 뒤 반환합니다.
    :house_position: 집의 위치
    :chicken_list: 모든 치킨집의 위치가 담긴 리스트
    """
    hx, hy = house_position
    chicken_distance = int(1e8)

    for cx, cy in chicken_list:
        chicken_distance = min(chicken_distance, abs(hx - cx) + abs(hy - cy))

    return chicken_distance


def get_city_chicken_distance(house_list, chicken_list):
    """
    도시 전체의 치킨 거리를 구한 뒤 반환합니다.
    :house_list: 모든 집의 위치가 담긴 리스트
    :chicken_list: 모든 치킨집의 위치가 담긴 리스트
    """
    city_chicken_distance = 0

    for house in house_list:
        city_chicken_distance += get_chicken_distance(house, chicken_list)

    return city_chicken_distance


# Main
# Input
n, m = map(int, input().split())
for x in range(n):
    temp = list(map(int, input().split()))
    for y, t in enumerate(temp):
        if t == 1:
            house.append((x, y))
        if t == 2:
            chicken.append((x, y))

answer = int(1e8)

# 치킨집 M개를 남길 수 있는 모든 조합을 만들어서 최단 치킨 거리 구하기
for chicken_list in list(combinations(chicken, m)):
    answer = min(answer, get_city_chicken_distance(house, chicken_list))
print(answer)
