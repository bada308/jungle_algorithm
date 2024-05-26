'''
https://www.acmicpc.net/problem/10844
'''
import sys
input = sys.stdin.readline

n = int(input())
# dp 테이블 선언 (행: 0 ~ N / 열: 0 ~ 9)
# 행: 계단 수의 길이 / 열: 1의 자리 숫자
dp = [[0] * (10) for _ in range(n+1)]

# 길이가 1인 경우 1로 초기화
# 0은 1로 초기화하면 안 된다. (0으로 시작하는 숫자는 계단 수가 아님)
for i in range(1, 10):
    dp[1][i] = 1

# dp 테이블 채우기
# 점화식: dp[n][k] = dp[n-1][k-1] + dp[n-1][k+1]
# 예외: k가 0 또는 9일 때
for i in range(2, n+1):
    for k in range(10):
        if k == 0:
            dp[i][k] = dp[i-1][k+1]
        elif k == 9:
            dp[i][k] = dp[i-1][k-1]
        else:
            dp[i][k] = dp[i-1][k-1] + dp[i-1][k+1]

# 정답을 1,000,000,000으로 나눈 나머지 출력
print(sum(dp[-1]) % 1000000000)
