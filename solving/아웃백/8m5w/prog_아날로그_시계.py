import math

# 각도 계산 상수
H = 1 / 120  # 시침이 1초에 움직이는 각도
M = 1 / 10   # 분침이 1초에 움직이는 각도
S = 6        # 초침이 1초에 움직이는 각도

def calcuate_angle(h, m, s):
    """시, 분, 초에 따른 각도 계산"""
    angle_h = 30 * (h % 12) + 0.5 * m + H * s # 시침의 각도 계산
    angle_m = 6 * m + M * s                   # 분침의 각도 계산
    angle_s = 6 * s                           # 초침의 각도 계산
    return angle_h, angle_m, angle_s

def count_overlaps(angle1, angle2, total_s, increment):
    """두 각도 사이의 겹치는 횟수 계산"""
    gap = 0
    count = 0
    while True:
        # 두 각도 사이의 겹치는 시간 계산
        temp = math.floor((gap - angle1 + angle2) / increment * 1000) / 1000 # 소수점 3자리 버림
        if temp < 0:
            gap += 360  # 겹치는 각도가 음수일 경우 360도 추가
        elif temp <= total_s:
            gap += 360  # 겹치는 각도가 총 시간 내에 있을 경우 360도 추가
            count += 1  # 겹치는 횟수 증가
        else:
            break
    return count

def solution(h1, m1, s1, h2, m2, s2):
    # 초기 각도 계산
    angle_h1, angle_m1, angle_s1 = calcuate_angle(h1, m1, s1)
    
    # 총 시간(초) 계산
    total_s = (h2 - h1) * 3600 + (m2 - m1) * 60 + (s2 - s1)
    
    # 시침 - 초침 겹치는 횟수
    answer = count_overlaps(angle_s1, angle_h1, total_s, S - H)
    
    # 분침 - 초침 겹치는 횟수
    answer += count_overlaps(angle_s1, angle_m1, total_s, S - M)
    
    # 시침 - 분침 - 초침 모두 겹치는 횟수 빼주기
    if (h1 == 0 and m1 == 0 and s1 == 0):
        answer -= 1 # 시작 시간이 0시 0분 0초일 경우 1번 빼기
    if (h1 == 12 and m1 == 0 and s1 == 0) or (h1 < 12 and h2 >= 12):
        answer -= 1 # 12시를 지날 경우 1번 빼기
    
    return answer