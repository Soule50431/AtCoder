import math

n= int(input())
ps = list(map(float, input().split()))

dp = [[0] * (n+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(1, n+1):
    dp[i][0] = dp[i-1][0] * (1 - ps[i-1])


for i in range(1, n+1):
    for j in range(1, n+1):
        if j > i:
            dp[i][j] = 0
        else:
            dp[i][j] = dp[i-1][j] * (1-ps[i-1]) + dp[i-1][j-1] * ps[i-1]
# print(dp)

ans = 0
for j in range(math.ceil(n/2), n+1):
    ans += dp[n][j]
print(ans)