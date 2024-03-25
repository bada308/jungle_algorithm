# https://www.acmicpc.net/problem/10872

import sys
input = sys.stdin.readline

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(int(input())))