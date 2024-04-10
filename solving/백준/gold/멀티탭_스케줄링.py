'''
https://www.acmicpc.net/problem/1700
멀티탭 스케줄링
'''

import sys
from collections import deque
input = sys.stdin.readline

def get_remove():
    result = 0
    for e in exist:
        if not use_info[e]:
            return e
        else:
            if use_info[result][0] < use_info[e][0]:
                result = e
    return result

n, k = map(int, input().split())
use_info = [deque() for _ in range(k+1)]
use_info[0].append(0)

sequence = list(map(int, input().split()))

for i in range(k):
    use_info[sequence[i]].append(i)

exist = set()
answer = 0

for s in sequence:
    if s not in exist:
        if len(exist) < n:
            exist.add(s)
        else:
            target = get_remove()
            exist.remove(target)
            exist.add(s)
            answer += 1
    use_info[s].popleft()

print(answer)