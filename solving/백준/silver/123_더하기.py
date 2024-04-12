'''
https://www.acmicpc.net/problem/9095
1, 2, 3 더하기
'''

import sys
input = sys.stdin.readline

dp = [1] + [0] * 12

for i in range(1, 12):
    for k in range(1, 4):
        if i - k >= 0:
            dp[i] += dp[i-k]

t = int(input())

for _ in range(t):
    n = int(input())
    print(dp[n])
