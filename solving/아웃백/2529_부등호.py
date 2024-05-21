'''
https://www.acmicpc.net/problem/2529
'''
import sys
input = sys.stdin.readline

n = int(input())
sign = list(input().split())

visited = set()
max_answer, min_answer = "", ""


def check(x, y, s):
    """주어진 두 숫자 x와 y 사이에 부등호 s가 성립하는지 확인

    Args:
        x (str): 비교할 첫 번째 숫자를 나타내는 문자열
        y (str): 비교할 두 번째 숫자를 나타내는 문자열
        s (str): 비교 연산자를 나타내는 문자열 ("<" 또는 ">")

    Returns:
        bool: 부등호 s가 x와 y 사이에서 성립하면 True, 그렇지 않으면 False
    """
    if s == "<":
        return int(x) < int(y)
    else:
        return int(x) > int(y)


def solve(count, current):
    """주어진 부등호 조건을 만족하는 가장 큰 수와 가장 작은 수를 찾는 재귀 함수

    Args:
        count (int): 현재까지 선택한 숫자의 개수
        current (str): 현재까지 만든 숫자를 나타내는 문자열
    """
    global max_answer, min_answer

    # 종료 조건 - 부등호 관계를 만족하는 k+1 자리의 정수가 되었을 때
    if count == n+1:
        if not min_answer:
            min_answer = current
        else:
            max_answer = current
        return

    for i in range(10):
        # 아직 선택되지 않은 숫자인 경우
        if i not in visited:
            # 첫 번째 숫자이거나, 이전 숫자와 현재 숫자가 주어진 부등호 관계를 만족하는 경우
            if count == 0 or check(current[-1], str(i), sign[count - 1]):
                visited.add(i)
                solve(count + 1, current + str(i))
                visited.remove(i)  # 백트래킹


solve(0, "")
print(max_answer)
print(min_answer)
