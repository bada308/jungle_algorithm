# https://www.acmicpc.net/problem/2504

from collections import deque

import sys
input = sys.stdin.readline

string = input().strip()
stack = deque()
inner = [[1, False] for _ in range(30)]
depth = 0
enable = True

for s in string:
    if s == ")":
        if not stack:
            enable = False
            break
        if stack[-1] == "(":
            stack.pop()
            value, visited = inner[depth - 1]
            if not visited:
                inner[depth - 1][0] = inner[depth][0] * 2
                inner[depth - 1][1] = True
                inner[depth] = [1, False]
            else:
                inner[depth - 1][0] += inner[depth][0] * 2
                inner[depth] = [1, False]
            depth -= 1
        else:
            enable = False
            break
    elif s == "]":
        if not stack:
            enable = False
            break
        if stack[-1] == "[":
            stack.pop()
            value, visited = inner[depth - 1]
            if not visited:
                inner[depth - 1][0] = inner[depth][0] * 3
                inner[depth - 1][1] = True
                inner[depth] = [1, False]
            else:
                inner[depth - 1][0] += inner[depth][0] * 3
                inner[depth] = [1, False]
            depth -= 1
        else:
            enable = False
            break
    else:
        stack.append(s)
        depth += 1

if not enable or len(stack) != 0:
    print(0)
else:
    print(inner[0][0])

'''
스택을 이용해서 풀었다.

아이디어는 좋다고 생각하는데 코드가 너무 복잡하다.
조금 더 코드를 단순하게 짤 수 있는 방법을 찾아보자!
'''