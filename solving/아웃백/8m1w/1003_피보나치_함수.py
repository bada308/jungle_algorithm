'''
https://www.acmicpc.net/problem/1003
'''
import sys
input = sys.stdin.readline

fibonacci = [(1, 0), (0, 1)]

t = int(input())

for __ in range(t):
    n = int(input())
    if n >= len(fibonacci):
        for i in range(len(fibonacci), n+1):
            fibonacci.append((fibonacci[i-1][0] + fibonacci[i-2][0], fibonacci[i-1][1] + fibonacci[i-2][1]))
    print(*fibonacci[n], sep=" ")