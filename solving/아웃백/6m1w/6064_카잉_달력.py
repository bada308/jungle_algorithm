'''
https://www.acmicpc.net/problem/6064
'''
import sys
import math
input = sys.stdin.readline

t = int(input())
for __ in range(t):
    m, n, x, y = map(int, input().split())
    max_value = math.lcm(m, n)

    b = x % n
    if b == 0:
        b = n
    answer = x

    while b != y:
        b = (b + m) % n
        if b == 0:
            b = n
        answer += m
        if (answer > max_value):
            answer = -1
            break

    print(answer)
