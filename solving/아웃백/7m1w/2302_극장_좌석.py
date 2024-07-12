'''
https://www.acmicpc.net/problem/2302
'''
import sys
input = sys.stdin.readline


n = int(input())
m = int(input())
vip = [int(input()) for __ in range(m)]


dp = [0] * (n + 2)
dp[1] = 1
dp[2] = 2

cur_idx = 1
answer = 1
for i in range(1, n + 2):
    if i in vip or i == n + 1:
        if cur_idx - 1:
            answer *= dp[cur_idx-1]
        cur_idx = 1
        continue
    if cur_idx == 1:
        dp[cur_idx] = 1
    elif cur_idx == 2:
        dp[cur_idx] = 2
    else:
        dp[cur_idx] = dp[cur_idx-1]+dp[cur_idx-2]
    cur_idx += 1

print(answer)
