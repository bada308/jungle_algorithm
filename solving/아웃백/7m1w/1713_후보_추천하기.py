'''
https://www.acmicpc.net/problem/1713
'''
import sys
input = sys.stdin.readline

N = int(input())
m = int(input())

nums = list(map(int, input().split()))

# 현재 사진틀에 게시된 학생들의 정보를 담는 딕셔너리
# { 학생 번호: [게시된 시기, 추천받은 횟수], ... }
dictionary = {}

for idx, n in enumerate(nums):
    key_list = dictionary.keys()  # 현재 사진틀에 게시된 학생 번호

    if n in key_list:  # case 1: 이미 게시된 학생인 경우
        dictionary[n][1] += 1  # 추천받은 횟수 증가
    else:  # case 2: 게시되지 않은 학생인 경우
        if len(key_list) == N:  # case 2-1: 비어있는 사진틀이 없는 경우

            # 사진틀에 게시된 학생 중 가장 추천 받은 횟수가 적은 학생 리스트 계산
            min_v = min(dictionary.values(), key=lambda x: x[1])[1]  # 최소 추천 수
            min_list = list(filter(
                lambda x: x[1][1] == min_v, dictionary.items()))  # 최소 추천 수에 해당하는 학생 리스트

            # 그 중 가장 오래된 사진 삭제
            victim = min(min_list, key=lambda x: x[1][0])[0]
            del dictionary[victim]
        dictionary[n] = [idx, 1]

print(*sorted(dictionary.keys()))
