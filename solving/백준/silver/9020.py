# https://www.acmicpc.net/problem/9020

import math
import sys
input = sys.stdin.readline

def getPrime(num):
    result = [False, False] + [True] * (num - 1)
    
    for i in range(2, int(math.sqrt(num)) + 1):
        for j in range(i * 2, num + 1, i):
                result[j] = False
    return result


prime10000 = getPrime(10000)
t = int(input())

for _ in range(t):
    n = int(input())
    result = []
    
    for i in range(2, len(prime10000)):
        if prime10000[i] is False:
            continue
        if i > (n // 2):
            break
        if prime10000[(n - i)]:
            result = [i, n - i]
    
    print(*result, sep=" ")