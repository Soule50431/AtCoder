h, w = map(int, input().split())
a = [input() for i in range(h)]

mod = 10**9 + 7
dp = [[0] * (w+1) for _ in range(h+1)]
dp[0][1] = 1
# print(dp)
for i in range(1, h+1):
    for j in range(1, w+1):
        if a[i-1][j-1] == "#":
            dp[i][j] = 0
        else:
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % mod
# print(dp)
print(dp[-1][-1])

