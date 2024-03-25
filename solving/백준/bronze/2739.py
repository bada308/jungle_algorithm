# https://www.acmicpc.net/problem/2739

import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, 10):
    print(f'{n} * {i} = {n * i}')