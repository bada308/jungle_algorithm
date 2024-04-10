'''
https://www.acmicpc.net/problem/1904
01타일
'''

import sys
input = sys.stdin.readline

n = int(input())

dp = [1, 2]



for i in range(2, n):
    dp.append((dp[i-2]+ dp[i-1]) % 15746)


print(dp[n-1])