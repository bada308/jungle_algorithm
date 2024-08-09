'''
https://school.programmers.co.kr/learn/courses/30/lessons/172927#
'''

def solution(picks, minerals):
    # 광물을 가중치 값으로 변환
    # 다이아몬드 : 25, 철 : 5, 돌 : 1
    conversion = {'diamond':25, 'iron':5, 'stone':1}
    minerals = [conversion[mineral] for mineral in minerals]
    
    weight_list = []
    
    # 광물 리스트를 5개씩 묶음
    for i in range(0, min(len(minerals), 5 * sum(picks)), 5):
        tmp = minerals[i:i+5]
        weight_list.append((sum(tmp), tmp))
    
    # 가중치 합을 기준으로 내림차순 정렬
    weight_list.sort(key=lambda x: x[0], reverse=True)
    
    answer = 0
    # 다이아 -> 철 -> 돌 곡괭이 순으로 사용
    # 다이아 피로도 = 광물의 가중치 // 25 | 철 피로도 = 광물의 가중치 // 5 | 돌 피로도 = 광물의 가중치 // 1
    for weight in weight_list:
        if sum(picks) == 0:
            break
        if picks[0] > 0:
            answer += sum(max((w // 25), 1) for w in weight[1])
            picks[0] -= 1
        elif picks[1] > 0:
            answer += sum(max((w // 5), 1) for w in weight[1])
            picks[1] -= 1
        else:
            answer += weight[0]
            picks[2] -= 1
    
    return answer