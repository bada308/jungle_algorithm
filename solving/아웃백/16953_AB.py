'''
https://www.acmicpc.net/problem/16953
'''
import sys
input = sys.stdin.readline

init, target = map(int, input().split())
answer = 0

# 문제와 반대로 target을 init으로 바꾸는 방식으로 문제 해결
while (target > init):
    # target이 양수일 경우 2로 나누기
    if (target % 2 == 0):
        target = target // 2
        answer += 1
    # target의 맨 오른쪽 숫자가 1인 경우 맨 오른쪽 숫자 제거
    elif (target % 10 == 1):
        target = target // 10
        answer += 1
    # 둘 다 만족하지 않는 경우 만들 수 없는 경우
    else:
        break


if (target == init):
    print(answer + 1)
else:
    print(-1)
