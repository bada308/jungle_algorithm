'''
https://www.acmicpc.net/problem/27436
'''
import sys
input = sys.stdin.readline

n = int(input())

sum = 1
count = 0
while sum < n:
    sum += count * 6
    count += 1

print(count)
