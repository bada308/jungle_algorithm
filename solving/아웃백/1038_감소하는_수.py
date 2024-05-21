'''
https://www.acmicpc.net/problem/1038
'''
import sys
from itertools import combinations
input = sys.stdin.readline

nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
result = []
for i in range(1, 11):
    temp = list(combinations(nums, i))
    for t in temp:
        result.append(int(''.join(map(str, t))))
result.sort()

n = int(input())

if n >= len(result):
    print(-1)
else:
    print(result[n])
