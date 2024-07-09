'''
https://www.acmicpc.net/problem/2170
'''
import sys
input = sys.stdin.readline

n = int(input())
lines = [sorted(list(map(int, input().split()))) for __ in range(n)]
lines.sort(key=lambda x: (x[0], x[1]))

answer = 0
min_v, max_v = lines[0][0], lines[0][1]
for i in range(1, n):
    if max_v < lines[i][0]:
        answer += (max_v - min_v)
        min_v, max_v = lines[i][0], lines[i][1]
        continue
    min_v = min(min_v, lines[i][0])
    max_v = max(max_v, lines[i][1])
answer += (max_v - min_v)
print(answer)
