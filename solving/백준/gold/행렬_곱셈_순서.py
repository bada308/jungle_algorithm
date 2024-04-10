'''
https://www.acmicpc.net/problem/11049
행렬 곱셈 순서
'''

import sys
input = sys.stdin.readline

n = int(input())
matrix = [tuple(map(int, input().split())) for _ in range(n)]
dp =[[0]*n for _ in range(n)]

for step in range(1, n):
    for start in range(0, n-step):
        end = start + step
        if step == 1:
            dp[start][end] = matrix[start][0] * matrix[start][1] * matrix[end][1]
            continue
        
        dp[start][end] = 2**32
        for k in range(start, end):
            dp[start][end] = min(dp[start][end], dp[start][k] + dp[k+1][end] + matrix[start][0] * matrix[k][1] * matrix[end][1])

print(dp[0][-1])