# https://www.acmicpc.net/problem/11053

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
stack = deque()
answer = 0

for n in nums:
    while stack and stack[-1] >= n:
        stack.pop()
    stack.append(n)
    answer = max(answer, len(stack))
    print(stack)

print(answer)