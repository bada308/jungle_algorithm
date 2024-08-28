def solution(edges):
    answer = [0, 0, 0, 0]
    count = 0
    for edge in edges:
        count = max(count, max(edge))
    
    out_in_degree = [[0, 0, i] for i in range(count + 1)]
    
    for a, b in edges:
        out_in_degree[a][0] += 1
        out_in_degree[b][1] += 1
    
    for out_d, in_d, node in out_in_degree:
        # 생성된 노드: 진출 차수가 2 이상이고 진입 차수가 0
        if out_d > 1 and in_d == 0:
            answer[0] = node
            continue
        
        # 막대 그래프 개수: 진출 차수가 0이고 진입 차수가 1 이상인 노드의 개수
        if out_d == 0 and in_d > 0:
            answer[2] += 1
            continue
        
        # 8자 그래프 개수: 진출 차수 진입 차수 모두 2 이상인 노드의 개수
        if out_d >= 2 and in_d >= 2:
            answer[3] += 1
            continue
    
    # 도넛 그래프 개수: 총 그래프의 개수 - 막대 그래프 개수 - 8자 그래프 개수
    answer[1] = out_in_degree[answer[0]][0] - answer[2] - answer[3]
    
    return answer