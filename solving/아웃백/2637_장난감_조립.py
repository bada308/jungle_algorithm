'''
https://www.acmicpc.net/problem/2637

배열 2개 집합 3개를 썼지만,,, 돌아가긴 하는군,,, 
'''
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

default_set = set([i for i in range(1, n+1)])  # 기본부품 집합
complement = set()  # 완제품 + 중간부품 집합

indegree = [0] * n  # 진입차수 배열
graph = {}  # 그래프 정보 딕셔너리

for i in range(m):
    x, y, k = map(int, input().split())

    # x 부품을 default 집합에서 제거 후 complement 집합에 추가
    if x in default_set:
        default_set.remove(x)
        complement.add(x)
    # y 부품에 대한 진입차수 +1
    indegree[y-1] += 1

    # 그래프 정보 추가
    if x in graph:
        graph[x].append((y, k))
    else:
        graph[x] = [(y, k)]

# 총 필요한 부품의 개수를 저장할 result 배열
result = [0] * (n+1)

# complement 집합이 공집합이 될 때까지 반복
while (complement):
    removed = set()

    for key in complement:
        # complement 집합에 있으면서 진입 차수가 0인 부품
        if indegree[key-1] == 0:
            if result[key] == 0:
                result[key] = 1
            # 해당 부품(key)이 필요로하는 부품의 수를 result에 추가
            for a, b in graph[key]:
                result[a] += result[key] * b
                indegree[a-1] -= 1  # 필요한 부품에 대한 진입 차수 1 감소
            indegree[key-1] = -1  # result에 추가한 key에 대해 진입 차수 -1로 변경
            removed.add(key)
    complement -= removed  # 해당 key를 complement에서 제거

# 기본 부품에 대해 (부품 번호, 필요한 개수) 출력
for d in default_set:
    print(d, result[d])
