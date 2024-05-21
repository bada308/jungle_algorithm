'''
https://www.acmicpc.net/problem/2253
'''

import sys
import math
input = sys.stdin.readline
INF = int(1e8)


def calculate(num):
    return math.ceil((2*num) ** 0.5)


# main
n, m = map(int, input().split())
small = set([int(input()) for _ in range(m)])
dp = [[INF]*(calculate(n)+1) for _ in range(n+1)]

dp[1][0] = 0

for i in range(2, n+1):
    if i in small:
        continue
    for step in range(1, calculate(i)):
        dp[i][step] = min(dp[i-step][step-1], dp[i-step]
                          [step], dp[i-step][step+1]) + 1


answer = min(dp[-1])

if answer == INF:
    print(-1)
else:
    print(answer)
