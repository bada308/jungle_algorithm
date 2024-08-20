'''
https://school.programmers.co.kr/learn/courses/30/lessons/181188#
'''

def solution(targets):
    # e를 기준으로 오름차순 정렬
    targets.sort(key=lambda x:x[1]) 

    answer = 1
    current_end = targets[0][1] # 현재 요격 미사일의 요격 가능 범위 끝점
    for s, e in targets:
        if s >= current_end: # 현재 요격 미사일로 요격 불가능한 경우
            answer += 1
            current_end = e # 새로운 요격 미사일의 요격 가능 범위 끝점 설정
    return answer