'''
https://www.acmicpc.net/problem/14888
연산자 끼워넣기
'''

import sys
import math
input = sys.stdin.readline

n = int(input())
피연산자 = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_answer = math.inf * -1
min_answer = math.inf

def solve(depth, value):
    global max_answer, min_answer, add, sub, mul, div
    if depth == n:
        max_answer = max(max_answer, value)
        min_answer = min(min_answer, value)
        return
    
    if add > 0:
        add -= 1
        solve(depth + 1, value + 피연산자[depth])
        add += 1
    if sub > 0:
        sub -= 1
        solve(depth + 1, value - 피연산자[depth])
        sub += 1
    if mul > 0:
        mul -= 1
        solve(depth + 1, value * 피연산자[depth])
        mul += 1
    if div > 0:
        div -= 1
        if value < 0:
            solve(depth + 1, ((value * -1) // 피연산자[depth]) * -1)
        else:
            solve(depth + 1, value // 피연산자[depth])
        div += 1

solve(1, 피연산자[0])

print(max_answer, min_answer, sep="\n")