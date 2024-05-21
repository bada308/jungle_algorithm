'''
https://www.acmicpc.net/problem/2294
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
dp = [int(1e8) for _ in range(k+1)]

dp[0] = 0

# 0원부터 k원까지 순회
for i in range(k+1):
    for coin in coins:
        # 현재 i원에서 coin의 가치를 더한 결과 업데이트
        if i + coin <= k:
            dp[i+coin] = min(dp[i+coin], dp[i] + 1)

# k원을 만들 수 없는 경우 -1 출력
if dp[k] == int(1e8):
    print(-1)
else:
    print(dp[k])
