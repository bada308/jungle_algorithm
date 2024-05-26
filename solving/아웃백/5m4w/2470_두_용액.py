'''
https://www.acmicpc.net/problem/2470
'''
import sys
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))

liquids.sort(key=lambda x: abs(x))  # 절대값 기준으로 정렬

start, end = 0, 0
answer = int(1e10)
result = []

for i in range(1, n):
    if abs(liquids[i] + liquids[i-1]) < answer:
        answer = abs(liquids[i] + liquids[i-1])
        result = [liquids[i-1], liquids[i]]

print(*sorted(result), sep=" ")
