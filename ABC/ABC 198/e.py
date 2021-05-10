from collections import Counter
import sys
sys.setrecursionlimit(10**5)


def dfs(u, parent):
    # print(u, "child:", nodes[u], seen_nodes)
    color = c[u]
    if seen_nodes[color] == 0:
        good[u] = True
        ans.append(u)
    seen_nodes[color] += 1
    for child in nodes[u]:
        if child == parent:
            continue
        dfs(child, u)
    seen_nodes[color] -= 1


n = int(input())
c = [-1] + list(map(int, input().split()))
# print(n, c)

nodes = [list() for i in range(n+1)]

seen_nodes = Counter()
good = [False] * (n+1)
ans = []

for i in range(n-1):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)
# print(nodes)

dfs(1, -1)
# for i, is_good in enumerate(good):
#     if is_good:
#         print(i)

print("\n".join(map(str, sorted(ans))))