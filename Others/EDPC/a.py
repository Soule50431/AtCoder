n = int(input())
h = list(map(int, input().split()))

dp = [float("INF") for i in range(n)]


def chmin(dp, i, x):
    if dp[i] > x:
        dp[i] = x
        return True
    return False


dp[0] = 0
for i in range(1, n):
    chmin(dp, i, + abs(h[i] - h[i-1]) + dp[i-1])
    chmin(dp, i, abs(h[i] - h[max(0, i-2)]) + dp[max(0, i-2)])
    # print(dp)

print(dp[-1])
