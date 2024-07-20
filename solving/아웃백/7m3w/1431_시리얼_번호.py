'''
https://www.acmicpc.net/problem/1431
'''
import sys
input = sys.stdin.readline

numbers = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])


n = int(input())
serialList = [input().strip() for _ in range(n)]
formatted = []

for serial in serialList:
    sumSerial = 0
    for s in list(serial):
        if s in numbers :
            sumSerial += int(s)
    formatted.append((len(serial), sumSerial, serial))

formatted.sort()
for f in formatted:print(f[2])