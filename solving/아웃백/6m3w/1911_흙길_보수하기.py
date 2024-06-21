'''
https://www.acmicpc.net/problem/1911
'''
import sys
input = sys.stdin.readline


n, l = map(int, input().split())
infos = sorted([tuple(map(int, input().split())) for _ in range(n)])

answer = 0
last = -1
for info in infos:
    start, end = info
    if (end <= last):
        continue
    start = max(last, start)

    count = (end - start + l - 1) // l
    last = start + count * l
    answer += count


print(answer)
