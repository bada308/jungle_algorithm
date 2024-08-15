'''
https://www.acmicpc.net/problem/1699

자연수 N을 제곱수의 합으로 나타낼 때 제곱수 항의 최소 개수 구하기

7 = 1 + 1 + 1 + 4
1 = 1
4 = 4
11 = 1 + 1 + 9
13 = 4 + 9

## 그리디인가???
→ 틀렸습니다. / 문제가 너무 쉬워보이면 함정이다...(https://www.acmicpc.net/board/view/144882)

## DP?
dp[i] = min(dp[j] + dp[i-j]), j는 i보다 작은 제곱 수
dp[0] = 0, dp[1] = 1
-> 시간이 6984ms나 걸림! PyPy3로 하니까 176ms

'''
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
for i in range(1, n + 1):
    min_value = float('inf')
    for j in range(1, int(i**0.5) + 1):
        square = j**2
        min_value = min(min_value, dp[i - square] + 1)
    dp[i] = min_value
print(dp[-1])