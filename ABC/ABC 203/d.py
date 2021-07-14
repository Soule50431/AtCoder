n, k = map(int, input().split())

inputs = [list(map(int, input().split())) for _ in range(n)]
# inputs = list(zip(*inputs))


def check(x):
    # 情報を圧縮
    bits = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            bit = 1 if inputs[i][j] > x else 0
            bits[i+1][j+1] = bit

    # 二次元累積和を計算
    for i in range(n+1):
        for j in range(n):
            bits[i][j+1] += bits[i][j]

    for j in range(n+1):
        for i in range(n):
            bits[i+1][j] += bits[i][j]

    for i in range(k, n+1):
        for j in range(k, n+1):
            if (bits[i][j] - bits[i][j-k] - bits[i-k][j] + bits[i-k][j-k]) < (k**2//2) + 1:
                return True
    return False


ok = 10**9+1
ng = -1

while ok - ng > 1:
    mid = (ok + ng) // 2
    # print("mid", mid)
    if check(mid):
        ok = mid
    else:
        ng = mid
    # print(ok, ng, mid)
print(ok)
