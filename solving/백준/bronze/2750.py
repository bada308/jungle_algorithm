# https://www.acmicpc.net/problem/2750

import sys
input = sys.stdin.readline

n = int(input())

nums = []
for i in range(n):
    nums.append(int(input()))

print(*sorted(nums), sep="\n")
