'''
https://www.acmicpc.net/problem/20438
'''
# import sys
# input = sys.stdin.readline

# n, k, q, m = map(int, input().split())
# sleep = set(list(map(int, input().split())))
# receiver = list(map(int, input().split()))

# result = [1] * (n + 3)

# for r in receiver:
#     if r in sleep:
#         continue
#     for i in range(r, n+3, r):
#         if i not in sleep:
#             result[i] = 0

# for _ in range(m):
#     start, end = map(int, input().split())
#     print(sum(result[start:end+1]))


import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split())
sleep = set(list(map(int, input().split())))
receiver = list(map(int, input().split()))

result = [1] * (n + 3)

for r in receiver:
    if r in sleep:
        continue
    for i in range(r, n+3, r):
        if i not in sleep:
            result[i] = 0

prefix_sum = [0] * (n+3)

for i in range(3, n+3):
    prefix_sum[i] = prefix_sum[i-1] + result[i]

for _ in range(m):
    start, end = map(int, input().split())
    print(prefix_sum[end] - prefix_sum[start-1])
