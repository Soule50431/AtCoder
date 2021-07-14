import math

n = int(input())
ts = list(map(int, input().split()))

sum_ = sum(ts)
dp = [[False]*(sum_+1) for _ in range(n+1)]

dp[0][0] = True

for i in range(n):
    for t in range(sum_+1):
        # 品物を選ぶ時
        if t - ts[i] >= 0:
            dp[i+1][t] |= dp[i][t-ts[i]]
        # 品物を選ばない時
        dp[i+1][t] |= dp[i][t]

for t in range(math.ceil(sum_/2), sum_+1):
    if dp[-1][t]:
        print(t)
        exit()

