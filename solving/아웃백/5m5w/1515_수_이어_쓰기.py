'''
https://www.acmicpc.net/problem/1515
'''
import sys
from collections import deque
input = sys.stdin.readline

n = deque(list(input().strip()))

result = 0
while n:
    result += 1
    for x in str(result):
        if x == n[0]:
            n.popleft()
        if not n:
            break

print(result)
