'''
https://www.acmicpc.net/problem/2493

앞에서부터 차례대로 스택에 push
push하기 전에 스택의 top에 담긴 탑의 높이가 cur의 높이보다 높을 때까지 pop
'''

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

stack = []
answer = []

for i in range(n):
    height = nums[i]
    while stack and stack[-1][0] < height:
        stack.pop()
    if len(stack) == 0:
        answer.append(0)
    else:
        answer.append(stack[-1][1])
    stack.append((nums[i], i+1))

print(*answer, sep=" ")
