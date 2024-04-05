'''
https://www.acmicpc.net/problem/2748
피보나치 수 2
'''

import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

def solve(n):
    if dp[n]:
        return dp[n]
    else:
        if n == 1 or n == 2:
            dp[n] = 1
        else:
            dp[n] = solve(n-1) + solve(n-2)
        return dp[n]

solve(n)
print(dp[n])