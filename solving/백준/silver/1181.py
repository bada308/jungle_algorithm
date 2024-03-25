# https://www.acmicpc.net/problem/1181

import sys
input = sys.stdin.readline

input_set = set()

n = int(input())
for _ in range(n):
    input_set.add(input().strip())

input_list = list(input_set)

print(*sorted(input_list, key=lambda x: (len(x), x)), sep="\n")
