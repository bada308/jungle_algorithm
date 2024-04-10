'''
https://www.acmicpc.net/problem/11047
동전 0
'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.reverse()

answer = 0
for coin in coins:
    count = k // coin
    if count > 0:
        answer += count
        k -= count * coin
print(answer)