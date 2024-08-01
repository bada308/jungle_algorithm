'''
https://www.acmicpc.net/problem/1747
'''
import sys
input = sys.stdin.readline
N = 1003001

result = [True] * (N + 1)
result[0] = False
result[1] = False
# 소수 필터
for i in range(2, N + 1):
    if result[i]:
        temp = 2
        while temp * i < N:
            result[i*temp] = False
            temp += 1
        if str(i) != str(i)[::-1]:
            result[i] = False


n = int(input())

for i in range(n, N+1):
    if result[i]:
        print(i)
        break

