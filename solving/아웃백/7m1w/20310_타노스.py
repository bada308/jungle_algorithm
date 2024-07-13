'''
https://www.acmicpc.net/problem/20310
'''
import sys
input = sys.stdin.readline

s = input().strip()
zero_count, one_count = s.count('0'), s.count('1')
zero_temp, one_temp = zero_count, one_count
answer = []

for i in range(len(s)):
    if s[i] == '1':
        if one_temp <= one_count // 2:
            answer.append('1')
        one_temp -= 1
    if s[i] == '0':
        if zero_temp > zero_count//2:
            answer.append('0')
        zero_temp -= 1

print(*answer, sep='')
