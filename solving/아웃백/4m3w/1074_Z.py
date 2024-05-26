'''
https://www.acmicpc.net/problem/1074
'''

import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())


answer = 0


def getCount(size, r, c):
    if size <= 0:
        return 0

    half = 2**(size-1)

    if (r < half and c < half):
        return 0 * half * half + getCount(size-1, r, c)
    elif (r < half and c >= half):
        return 1 * half * half + getCount(size-1, r, c - half)
    elif (r >= half and c < half):
        return 2 * half * half + getCount(size-1, r - half, c)
    else:
        return 3 * half * half + getCount(size-1, r - half, c - half)


print(getCount(n, r, c))
