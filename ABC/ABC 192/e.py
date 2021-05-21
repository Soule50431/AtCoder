from heapq import heapify, heappop, heappush
import math

# 入力
n, m, x, y = map(int, input().split())
x -= 1
y -= 1

# グラフ作成
edges = [[] for i in range(n)]
for i in range(m):
    a, b, t, k = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append([b, t, k])
    edges[b].append([a, t, k])

print(edges)
# Dijkstra
dists = [float("INF")] * n

queue = [(0, x)]
heapify(queue)

while queue:
    cost, u = heappop(queue)

    # 更新不可の場合
    if cost > dists[u]:
        continue

    # 隣接ノードを見る
    for node, t, k in edges[u]:
        temp = math.ceil(cost/k)
        time = temp * t
        if dists[node] > time:
            dists[node] = time
            heappush(queue, (time, node))

print(dists)
if dists[y] == float("INF"):
    print(-1)
else:
    print(dists[y])