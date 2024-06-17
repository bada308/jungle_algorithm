'''
https://www.acmicpc.net/problem/13335
'''
import sys
from collections import deque
input = sys.stdin.readline

n, w, l = map(int, input().split())
weights = list(map(int, input().split()))


answer = 0
queue = deque([0 for __ in range(w)])
idx = 0

while (queue):
    cur_w = queue.popleft()
    l += cur_w
    answer += 1
    if idx < n:
        if weights[idx] <= l:
            queue.append(weights[idx])
            l -= weights[idx]
            idx += 1
        else:
            queue.append(0)

print(answer)
