'''
https://www.acmicpc.net/problem/1931
회의실 배정
'''

import sys
input = sys.stdin.readline

n = int(input())

table = []

for _ in range(n):
    s, e = map(int, input().split())
    table.append((s, e))

table.sort(key=lambda x:(x[1], x[0]))

answer = 1
end = table[0][1]

for i in range(1, n):
    if table[i][0] >= end:
        answer += 1
        end = table[i][1]

print(answer)