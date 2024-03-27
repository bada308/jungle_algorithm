from collections import deque
import sys
input = sys.stdin.readline

def grade(d, score):
    _, visited = inner[d - 1]
    if not visited:
        inner[d - 1][0] = inner[d][0] * score
        inner[d - 1][1] = True
    else:
        inner[d - 1][0] += inner[d][0] * score
    inner[d] = [1, False]

string = input().strip()
stack = deque()


inner = [[1, False] for _ in range(16)]
depth = 0
score_dict = {
    ')' : ('(', 2),
    ']' : ('[', 3)
}

for s in string:
    if s in score_dict:
        if not stack or stack[-1] != score_dict[s][0]:
            print(0)
            sys.exit(0)
        stack.pop()
        grade(depth, score_dict[s][1])
        depth -= 1
    else:
        stack.append(s)
        depth += 1

if depth > 0:
    print(0)
else:
    print(inner[0][0])