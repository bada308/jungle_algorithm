'''
https://www.acmicpc.net/problem/1057
'''
import sys
input = sys.stdin.readline

n, kim, lm = map(int, input().split())
answer = 0

while kim != lm:
    kim = (kim + 1) // 2
    lm = (lm + 1) // 2
    answer += 1

print(answer)
