n, w = map(int, input().split())
goods = [list(map(int, input().split())) for i in range(n)]

# print(goods)


def chmin(dp, i, x):
    if dp[i] > x:
        dp[i] = x
        return True
    return False


V_MAX = 10**3 * n
dp = [[float("INF")]*(V_MAX+1) for i in range(n+1)]
dp[0][0] = 0

for i in range(n):
    for v in range(V_MAX+1):
        # 品物を選択
        # print(i,v)
        if v - goods[i][1] >= 0:
            chmin(dp[i+1], v, dp[i][v - goods[i][1]] + goods[i][0])
        # 品物を選択しない場合
        chmin(dp[i+1], v, dp[i][v])
# for i in range(len(dp)):
#     print(dp[i])
ans = 0
for v in range(V_MAX+1):
    if dp[n][v] <= w:
        ans = v
print(ans)