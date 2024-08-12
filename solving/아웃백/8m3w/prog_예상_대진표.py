'''
https://school.programmers.co.kr/learn/courses/30/lessons/12985
'''

def solution(n,a,b):
    answer = 1
    
    while abs(a-b) != 1 or max(a, b) % 2 != 0:
        answer += 1
        a = (a+1) // 2
        b = (b+1) // 2

    return answer