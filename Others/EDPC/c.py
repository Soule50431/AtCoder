n = int(input())
days = [list(map(int, input().split())) for i in range(n)]


def chmax(dp, i, x):
    if dp[i] < x:
        dp[i] = x
        return True
    return False


dp = [[-1, -1, -1] for i in range(n)]

dp[0] = days[0]
for i in range(1,n):
    chmax(dp[i], 0, max(dp[i-1][1], dp[i-1][2]) + days[i][0])
    chmax(dp[i], 1, max(dp[i-1][0], dp[i-1][2]) + days[i][1])
    chmax(dp[i], 2, max(dp[i-1][0], dp[i-1][1]) + days[i][2])
print(max(dp[-1]))

