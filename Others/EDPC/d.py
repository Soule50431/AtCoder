n, W = map(int, input().split())
goods = [[0, 0]]
goods.extend([list(map(int, input().split())) for i in range(n)])

dp = [[0]*(W+1) for i in range(n+1)]

# print(goods)

def chmax(dp, i, x):
    if dp[i] < x:
        dp[i] = x
        return True
    return False


for i in range(1, n+1):
    for w in range(1, W+1):
        # 品物iを選択
        if w - goods[i][0] >= 0:
            chmax(dp[i], w, dp[i-1][w - goods[i][0]] + goods[i][1])
        # 品物を選ばない
        chmax(dp[i], w, dp[i-1][w])
print(dp[-1][-1])

