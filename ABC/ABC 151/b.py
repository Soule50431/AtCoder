n, k, m = map(int, input().split())
a = list(map(int, input().split()))

diff = n * m - sum(a)
if diff <= k:
    print(max(0, diff))
else:
    print(-1)