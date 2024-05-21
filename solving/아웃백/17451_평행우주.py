'''
https://www.acmicpc.net/problem/17451
'''
import sys
input = sys.stdin.readline

n = int(input())
speeds = list(map(int, input().split()))

speed = speeds[-1]

for i in range(n-2, -1, -1):
    if (speed < speeds[i]):
        print
    else:
        print
print(speed)
