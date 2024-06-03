'''
https://www.acmicpc.net/problem/2410
'''
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):
    if i % 2 == 0:
        dp[i] = dp[i-1] + dp[i//2]
    else:
        dp[i] = dp[i-1]

print(dp[-1] % 1000000000)
