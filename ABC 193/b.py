n = int(input())

min_ = float("INF")
for _ in range(n):
    a, p, n = list(map(int, input().split()))
    if n - a > 0:
        min_ = min(min_, p)

print(-1 if min_ == float("INF") else min_)
