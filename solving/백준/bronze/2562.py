# https://www.acmicpc.net/problem/2562

import sys
input = sys.stdin.readline

input_list = [int(input()) for _ in range(9)]

max_value = max(input_list)
print(max_value)
print(input_list.index(max_value) + 1)