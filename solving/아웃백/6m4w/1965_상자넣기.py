'''
https://www.acmicpc.net/problem/1965
'''
import sys
input = sys.stdin.readline

n = int(input())
boxs = list(map(int, input().split()))
dp = [0 for __ in range(n)]

for i in range(0, n):
    max_value = 0
    for j in range(i):
        if boxs[j] < boxs[i]:
            max_value = max(max_value, dp[j])
    dp[i] = max_value + 1

print(max(dp))
