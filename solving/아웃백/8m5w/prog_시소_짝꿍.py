from collections import defaultdict
import math

def solution(weights):
    answer = 0
    w_dict = defaultdict(int)
    
    # 몸무게 별 명수 확인
    for w in weights:
        w_dict[w] += 1
        
    # 몸무게가 동일한 시소 짝꿍 구하기
    for key, value in w_dict.items():
        if value > 1:
            answer += math.comb(value, 2)

    # 몸무게가 다른 시소 짝꿍 구하기
    w_list = list(w_dict.keys())
    for i in range(len(w_list)):
        for j in range(i + 1, len(w_list)):
            k1, k2 = w_list[i], w_list[j]
            v1, v2 = w_dict[k1], w_dict[k2]
            if k1 / k2 in {1/2, 2/3, 3/4, 4/3, 3/2, 2}:
                answer += v1 * v2
    return answer