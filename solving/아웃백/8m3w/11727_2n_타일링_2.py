'''
https://www.acmicpc.net/problem/11727

2xn 크기의 직사각형을 채우는 방법의 수를 10007로 나눈 나머지 구하기
- 타일: 1x2, 2x1, 2x2
- 2x2 1개 = 2x1 타일 2개

예제)
8
1 * 8 + 2 * 0 -> 8C0 * 2^0 = 1
1 * 6 + 2 * 1 -> 7C1 * 2^1 = 14
1 * 4 + 2 * 2 -> 6C2 * 2^2 = 60
1 * 2 + 2 * 3 -> 5C3 * 2^3 = 80
1 * 0 + 2 * 4 -> 4C4 * 2^4 = 16
'''
import sys
import math
input = sys.stdin.readline
mod = 10007


n = int(input())
answer = 0

for i in range(n, -1, -2):
    j = (n - i) // 2
    answer += math.comb(i+j, j) * (2**j)

print(answer % mod)