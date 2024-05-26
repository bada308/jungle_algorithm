'''
https://www.acmicpc.net/problem/14501
'''
import sys
input = sys.stdin.readline

n = int(input())
schedule = []

for i in range(1, n+1):
    t, p = map(int, input().split())
    if i + t - 1 <= n:
        schedule.append((i + t - 1, i, p))

schedule.sort()
max_time = 0
answer = 0

for end, start, price in schedule:
    if start > max_time:
        answer += price
        max_time = end
        print(start, end, price)

print(answer)
