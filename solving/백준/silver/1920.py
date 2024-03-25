# https://www.acmicpc.net/problem/1920

import sys
input = sys.stdin.readline

n = int(input())
n_set = set(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

answer = []
for value in m_list:
    if value in n_set:
        answer.append(1)
    else:
        answer.append(0)

print(*answer, sep="\n")
