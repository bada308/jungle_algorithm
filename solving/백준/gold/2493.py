# https://www.acmicpc.net/problem/2493

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
top = list(map(int, input().split()))
stack = deque()

for i in range(n):
    result = 0
    while stack:
        if stack[-1][0] < top[i]:
            stack.pop()
        else:
            result = stack[-1][1]
            break
    print(result, end=" ")
    stack.append((top[i], i+1))