'''
숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현할 수 있다.
N 사용횟수의 최솟값을 구하자

어려운데.....?
'''

def solution(N, number):
    if N == number:
        return 1
    
    # dp[i]는 N을 i번 사용하여 만들 수 있는 모든 수의 집합
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        # N을 i번 반복하여 만든 수 추가
        dp[i].add(int(str(N) * i))
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i - j]:
                    dp[i].add(x + y)
                    dp[i].add(x * y)
                    if x - y > 0:
                        dp[i].add(x - y)
                    if y - x > 0:
                        dp[i].add(y - x)
                    if y and x // y > 0:
                        dp[i].add(x // y)
                    if x and y // x > 0:
                        dp[i].add(y // x)
                        
        # number가 dp[i]에 포함되어 있으면 i 반환
        if number in dp[i]:
            return i
    
    # 8번 이하로 표현할 수 없으면 -1 반환
    return -1
