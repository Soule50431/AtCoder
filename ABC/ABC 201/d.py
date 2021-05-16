h, w = map(int, input().split())
points = [[1 if char == "+" else -1 for char in input()] for i in range(h)]

dp = [[-float("INF")]*w for i in range(h)]


def chmax(dp, i, x):
    if dp[i] < x:
        dp[i] = x
        return True
    return False


for i in reversed(range(h)):
    for j in reversed(range(w)):
        if i == h-1 and j == w-1:
            dp[i][j] = 0
        if i + 1 < h:
            chmax(dp[i], j, points[i+1][j] - dp[i+1][j])
        if j + 1 < w:
            chmax(dp[i], j, points[i][j+1] - dp[i][j+1])

score = dp[0][0]
if score == 0:
    print("Draw")
elif score > 0:
    print("Takahashi")
elif score < 0:
    print("Aoki")

