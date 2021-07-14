n, m = map(int, input().split())

MOD = 10**9 +7

dp = [0] * (n+1)
for i in range(m):
    dp[int(input())] = -1
dp[0] = 1
for i in range(n+1):
    if dp[i] == -1:
        continue
    for j in range(1, 2+1):
        if i + j <= n and dp[i+j] != -1:
            dp[i+j] = (dp[i+j] + dp[i]) % MOD
print(dp[-1])
