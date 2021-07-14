n, m = map(int, input().split())

dists = [[float("inf")]*n for _ in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    dists[a][b] = c
for i in range(n):
    dists[i][i] = 0

# print(dists)
ans = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])
            ans += dists[i][j] if dists[i][j] != float("inf") else 0
# print(dists)
print(ans)
