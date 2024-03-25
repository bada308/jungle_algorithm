# https://www.acmicpc.net/problem/2751

import sys
input = sys.stdin.readline

n = int(input())

input_list = [int(input()) for _ in range(n)]
print(*sorted(input_list), sep="\n")