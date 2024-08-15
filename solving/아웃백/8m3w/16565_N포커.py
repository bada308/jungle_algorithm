'''
https://www.acmicpc.net/problem/16565
키워드: 포함 배제의 원리
'''
import sys
import math
input = sys.stdin.readline

MOD = 10007
N = int(input())

result = 0
cnt, pos = 1, 1 # cnt: 포카드의 수, pos: 부호

four_cnt = cnt * 4
while N - four_cnt >= 0:
  # math.comb(13,cnt): 포카드를 `cnt` 쌍 뽑는 경우의 수 
  # math.comb(52 - four_cnt, N - four_cnt): 남은 카드 중에서 `N - four_cnt` 개의 카드를 선택하는 경우의 수
  result += pos * math.comb(13,cnt) * math.comb(52-four_cnt, N-four_cnt)
  cnt += 1
  pos = -pos
  four_cnt += 4

print(result % MOD)
