n, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [float("INF") for i in range(n)]


def chmin(dp, i, x):
    if dp[i] > x:
        dp[i] = x
        return True
    return False


dp[0] = 0
for i in range(1, n):
    for k in range(1+K):
        if i - k >= 0:
            chmin(dp, i, abs(h[i]-h[i-k]) + dp[i-k])
        else:
            continue
    # print(dp)

print(dp[-1])
