# https://www.acmicpc.net/problem/10830

import sys
input = sys.stdin.readline

n, b = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

def multi(x, y):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += x[i][k] * y[k][j]
            result[i][j] %= 1000
    return result

def solution(a, b):
    if b == 1:
        return a
    
    tmp = solution(a, b//2)
    
    if b % 2 == 0:
        return multi(tmp, tmp)
    else:
        return multi(multi(tmp, tmp), a)

answer = solution(a, b)
for a in answer:
    for i in a:
        print(i%1000, end=" ")
    print()