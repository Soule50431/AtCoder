from collections import deque
n, k = map(int, input().split())

inputs = [list(map(int, input().split())) for _ in range(n)]
inputs = list(zip(*inputs))
# print(inputs)

lands_ = [[0]*(n-k+1) for _ in range(n-k+1)]
for i in range(n-k+1):
    for j in range(n):
        # print(i, j)
        lands_[i][n*j:n*j+k] = inputs[j][i:i+k]


lands = []
for land in lands_:
    lands.append(deque(land))

median = float("INF")

for land in lands:
    # print("land", land)
    temp = deque()
    for j in range(n-k+1):

        temp = sorted(temp, reverse=True)
        # print(temp)
        median = min(median, temp[(k**2)//2])
print(median)
