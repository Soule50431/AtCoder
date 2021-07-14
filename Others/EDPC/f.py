from collections import deque
s = input()
t = input()


def chmax(i, j, max):
    if dp[i][j] <= max:
        dp[i][j] = max
        return True
    return False


len_s = len(s)
len_t = len(t)
dp = [[0] * (len_t + 1) for _ in range(len_s + 1)]
dp_prev = [[(0, 0)] * (len_t + 1) for _ in range(len_s + 1)]
# print(dp)

for i in range(1, len_s+1):
    for j in range(1, len_t+1):
        diag = 1 if s[i-1] == t[j-1] else 0
        if chmax(i, j, dp[i-1][j]):
            dp_prev[i][j] = (i-1, j)
        if chmax(i, j, dp[i][j - 1]):
            dp_prev[i][j] = (i, j-1)
        if chmax(i, j, dp[i - 1][j - 1] + diag):
            dp_prev[i][j] = (i-1, j-1)


ans = deque()
cur = (len_s, len_t)

while True:
    cur_x, cur_y = cur
    prev = dp_prev[cur_x][cur_y]
    prev_x, prev_y = prev
    # print(cur, prev)
    # print(dp[cur_x][cur_y], dp[prev_x][prev_y])
    if dp[cur_x][cur_y] != dp[prev_x][prev_y]:
        ans.appendleft(s[cur_x-1])
    cur = prev
    if cur == (0, 0):
        break

# print(dp[-1][-1])
print("".join(ans))
