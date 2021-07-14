from collections import deque
# 入力
n, m = map(int, input().split())
edges = [list() for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)

dist = [[0] * n for _ in range(n)]
# bfs
for i in range(n):
    queue = deque([i])
    seen_node = set()

    while queue:
        cur = queue.popleft()
        seen_node.add(cur)
        dist[i][cur] = 1
        for child in edges[cur]:
            if child not in seen_node:
                queue.append(child)
# print(dist)
ans = 0
for i in range(n):
    for j in range(n):
        ans += dist[i][j]
print(ans)
