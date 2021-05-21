import sys
sys.setrecursionlimit(10**6)
h, w = map(int, input().split())

points = [[1 if char == "+" else -1 for char in input()] for i in range(h)]

visited = [[False]*w for i in range(h)]
memo = [[0]*w for i in range(h)]


def f(i, j):
    if i == h-1 and j == w-1:
        return 0
    if visited[i][j]:
        return memo[i][j]
    visited[i][j] = True

    res = -float("INF")
    if i + 1 < h:
        res = max(res, points[i+1][j] - f(i+1, j))
    if j + 1 < w:
        res = max(res, points[i][j+1] - f(i, j+1))
    memo[i][j] = res
    return res


ans = f(0, 0)
if ans == 0:
    print("Draw")
elif ans > 0:
    print("Takahashi")
elif ans < 0:
    print("Aoki")

