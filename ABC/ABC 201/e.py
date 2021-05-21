import sys
sys.setrecursionlimit(10**7)

n = int(input())
edges = [list() for _ in range(n)]

mod = 10**9 + 7

for i in range(n-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append((v, w))
    edges[v].append((u, w))

# print(edges)
# print(weights)

dist = [-1]*n
dist[0] = 0

# stack = [0]
# while stack:
#     u = stack.pop()
#     for child, weight in edges[u]:
#         if dist[child] != -1:
#             continue
#         dist[child] = dist[u] ^ weight
#         stack.append(child)

def dfs(u):
    for child, weight in edges[u]:
        if dist[child] != -1:
            continue
        dist[child] = dist[u] ^ weight
        dfs(child)
dfs(0)
# print(dist)

ones = [0]*60
for i in range(n):
    for j in range(60):
        if (dist[i] >> j) & 1 == 1:
            ones[j] += 1

# print(ones)
ans = 0
for i in range(60):
    ans += ones[i] * (n - ones[i]) * (1 << i)
    ans %= mod
    # print(ans)
    # print(weights)

print(ans)
