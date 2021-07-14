n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

MOD = 10**9 + 7

def popcount(x):
    '''xの立っているビット数をカウントする関数
    (xは64bit整数)'''

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
    x = x + (x >> 8) # 16bitごと
    x = x + (x >> 16) # 32bitごと
    x = x + (x >> 32) # 64bitごと = 全部の合計
    return x & 0x0000007f

def bits(n, k):
    if (n >> k) & 1 == 1:
        return True
    else:
        return False

dp = [0] * (1 << n)
dp[0] = 1

for s in range(1, 1 << n):
    i = popcount(s)
    for j in range(n):
        if bits(s, j) and a[i-1][j] == 1:
            dp[s] = (dp[s] + dp[s ^ (1 << j)]) % MOD
print(dp[(1 << n) - 1] % MOD)
