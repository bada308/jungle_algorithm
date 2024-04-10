'''
https://www.acmicpc.net/problem/1946
신입 사원
'''

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    scores = [tuple(map(int, input().split())) for _ in range(n)]
    scores.sort()
    answer = 1
    
    min_score = scores[0][1]
    for i in range(1, n):
        if min_score >= scores[i][1]:
            answer += 1
            min_score = scores[i][1]
    print(answer)