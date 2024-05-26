'''
https://www.acmicpc.net/problem/1967
'''

n = int(input())
tree = {}
answer = [0] * (n+1)
max_a = [0] * (n+1)

while (1):
    try:
        parent, child, weight = map(int, input().split())
        if parent not in tree.keys():
            tree[parent] = []
        tree[parent].append((child, weight))
    except:
        break


def solve(node):
    if node not in tree.keys():
        return 0
    child_count = len(tree[node])

    value = []
    if (child_count == 2):
        value.append(solve(tree[node][1][0]) + tree[node][1][1])
    value.append(solve(tree[node][0][0]) + tree[node][0][1])

    max_a[node] = max(value)
    return max_a[node]


solve(1)
print(max_a)

for key in tree.keys():
    for ch, cnt in tree[key]:
        answer[key] += (max_a[ch] + cnt)
print(answer)
print(max(answer))
