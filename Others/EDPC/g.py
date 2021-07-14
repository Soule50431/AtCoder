from collections import deque

n, m = map(int, input().split())
graph = [list() for _ in range(n)]
indegree = [0] * n

# 隣接リストと入次数のリストを作成
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append(y)
    indegree[y] += 1

# print(indegree)
# print(graph)

# トポロジカルソート
sorted_vertices = []
queue = deque()

# 入次数0の頂点をキューに追加
for node in range(n):
    if indegree[node] == 0:
        queue.append(node)

while queue:
    v = queue.popleft()

    for node in graph[v]:
        indegree[node] -= 1
        if indegree[node] == 0:
            queue.append(node)

    sorted_vertices.append(v)
# print(sorted_vertices)

dp = [0] * n


def chmax(i, *maxes):
    dp[i] = max(maxes)


for node in sorted_vertices:
    for child in graph[node]:
        chmax(child, dp[node] + 1)
        
ans = 0
for i in range(n):
    ans = max(ans, dp[i])
print(ans)