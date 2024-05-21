'''
https://www.acmicpc.net/problem/1697
'''
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

d = deque([])
visit = set()
d.append((n, 0))
visit.add(n)

while (d):
    num, depth = d.popleft()

    if num == k:
        print(depth)
        break

    if num - 1 not in visit and num - 1 >= 0:
        d.append((num-1, depth + 1))
        visit.add(num-1)
    if num+1 <= 100000 and num + 1 not in visit:
        d.append((num+1, depth+1))
        visit.add(num+1)
    if num < k and num * 2 not in visit:
        d.append((2*num, depth + 1))
        visit.add(num*2)
