'''
https://www.acmicpc.net/problem/1309
'''
import sys
input = sys.stdin.readline

n = int(input())

count = 0

dp = [[0]*3 for _ in range(n)]

for i in range(3):
    dp[0][i] = 1

for i in range(1, n):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901

answer = sum(dp[-1])

print(answer % 9901)
