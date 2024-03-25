# https://www.acmicpc.net/problem/1629

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def getMod(a, b, c):
    if b == 1:
        return a ** b % c
    
    if b % 2 == 0:
        return (getMod(a, b//2,c) ** 2) % c
    else:
        return (getMod(a, b//2, c) ** 2 * a) % c

print(getMod(a, b, c))