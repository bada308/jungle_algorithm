'''
https://www.acmicpc.net/problem/2253
점프
'''

# import sys
# input = sys.stdin.readline

# def get_aprx(num):
#     return int((2*num)**0.5)

# n, k = map(int, input().split())
# small = set([int(input()) for _ in range(k)])

# dp = [[10001] * (get_aprx(n) + 2) for _ in range(n+1)]
# dp[1][0] = 0

# for i in range(2, n+1):
#     if i in small:
#         continue
#     for v in range(1, get_aprx(i) + 1):
#         dp[i][v] = min(dp[i-v][v-1], dp[i-v][v], dp[i-v][v+1]) + 1

# answer = min(dp[n])
# if answer == int(10001):
#     print(-1)
# else:
#     print(answer)


# ------------------------

import sys
input = sys.stdin.readline

def get_aprx(num):
    return int((2*num)**0.5)

n, m = map(int, input().split())
small = set([int(input()) for _ in range(m)])
dp = [[10001]*(get_aprx(n)+2) for _ in range(n+1)]

dp[1][0] = 0

for i in range(1, n+1):
    if i in small:
        continue
    for v in range(1, get_aprx(i)+1):
        if i-v >= 0 and (i-v) not in small:
            dp[i][v] = min(dp[i-v][v-1], dp[i-v][v], dp[i-v][v+1]) + 1

answer = min(dp[-1])

if answer == 10001: print(-1)
else: print(answer)