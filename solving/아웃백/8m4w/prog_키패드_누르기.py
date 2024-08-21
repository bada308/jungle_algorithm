'''
파이썬 기말고사 문제 였는뎅 ㅎㅎ 반갑다!!

왼쪽 열 -> 왼손
오른쪽 열 -> 오른손
가운데 열 -> 더 가까운 손가락, 만약 거리 같으면 본인 주손 사용

* => 10 / 0 => 11 / # => 12

거리를 어떻게 구하징
x 좌표 나머지, y 좌표 몫
'''

def solution(numbers, hand):
    # 0 => 11
    for i in range(len(numbers)):
        if numbers[i] == 0: numbers[i] = 11
    
    # 거리 계산 함수
    def distance(pos1, pos2):
        return abs((pos1 - 1) % 3 - (pos2 - 1) % 3) + abs((pos1 - 1) // 3 - (pos2 - 1) // 3)
    
    # * => 10, # => 12
    left, right = 10, 12
    answer = ''
    for num in numbers:
        if num % 3 == 1:
            # 왼쪽 열
            left = num
            answer += 'L'
        elif num % 3 == 0:
            # 오른쪽 열
            right = num
            answer += 'R'
        else:
            # 가운데 열
            l_dist, r_dist = distance(left, num), distance(right, num)
            
            if l_dist < r_dist:
                # 왼손이 더 가까울 때
                left = num
                answer += 'L'
            elif l_dist > r_dist:
                # 오른손이 더 가까울 때
                right = num
                answer += 'R'
            else:
                # 거리가 같을 때 -> 주손 사용
                if hand == 'left':
                    left = num
                    answer += 'L'
                else:
                    right = num
                    answer += 'R'
    return answer