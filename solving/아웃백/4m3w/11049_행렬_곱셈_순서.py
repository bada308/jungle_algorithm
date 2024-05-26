'''
https://www.acmicpc.net/problem/11049
'''
import sys
input = sys.stdin.readline

n = int(input())
matrix_info = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

# for start in range(n):
#     for step in range(1, n - start):
#         end = start + step
#         if step == 1:
#             dp[start][end] = matrix_info[start][0] * \
#                 matrix_info[end][0] * matrix_info[end][1]
#             continue
# min_value = int(1e8)
# for k in range(start, end):
#     min_value = min(min_value, dp[start][k] + dp[k+1][end] +
#                     matrix_info[start][0] *
#                     matrix_info[k][1] * matrix_info[end][1])
# dp[start][end] = min_value

for step in range(1, n):
    for start in range(n):
        end = start + step
        if end >= n:
            continue
        if step == 1:
            dp[start][end] = matrix_info[start][0] * \
                matrix_info[end][0] * matrix_info[end][1]
            continue
        min_value = int(1e8)
        for k in range(start, end):
            min_value = min(min_value, dp[start][k] + dp[k+1][end] +
                            matrix_info[start][0] *
                            matrix_info[k][1] * matrix_info[end][1])
        dp[start][end] = min_value

print(dp[0][-1])
