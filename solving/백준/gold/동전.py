'''
https://www.acmicpc.net/problem/9084
동전
'''
# import sys
# input = sys.stdin.readline

# t = int(input())

# for _ in range(t):
#     n = int(input())
#     coins = map(int, input().split())
#     target = int(input())
#     dp = [1] + [0]*(target)

#     for coin in coins:
#         for i in range(1, target+1):
#             if i < coin:
#                 continue
#             else:
#                 dp[i] += dp[i-coin]

#     print(dp[-1])
