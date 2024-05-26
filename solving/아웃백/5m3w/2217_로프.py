'''
https://www.acmicpc.net/problem/2217
'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
rope = [int(input()) for _ in range(n)]
rope.sort()

answer = 0

for i in range(n):
    answer = max(answer, rope[i] * (len(rope) - i))

print(answer)
