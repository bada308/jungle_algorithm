'''
https://www.acmicpc.net/problem/11722
가장 긴 감소하는 부분 수열
'''
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    init = dp[i]
    for j in range(i):
        if nums[i] < nums[j]:
            dp[i] = max(dp[i], init + dp[j])

print(max(dp))
