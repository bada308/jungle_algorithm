''''
https://www.acmicpc.net/problem/15486
퇴사2
'''

import sys
input = sys.stdin.readline

n = int(input())
end_info = [[] for _ in range(n+1)]
dp = [0]*(n+1)

for i in range(1, n+1):
    t, p = map(int, input().split())
    if i + t <= n+1:
        end_info[i+t-1].append((t, p))

for day in range(1, n+1):
    dp[day] = dp[day-1]
    if end_info[day]:
        for ti, pi in end_info[day]:
            dp[day] = max(dp[day], pi + dp[day-ti])

print(dp[-1])
