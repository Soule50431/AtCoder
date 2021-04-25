import math

A, B, W = list(map(int, input().split()))

w = W * 1000
# print(A, B, w)

min_count = math.ceil(w/B)
max_count = math.floor(w/A)

max_ = None
min_ = None

for i in range(min_count, max_count+1):
    # 最小値
    if w >= A * i:
        min_ = i
        break

for j in reversed(range(min_count, max_count+1)):
    # 最大値
    if w <= B * j:
        max_ = j
        break

if min_ is None or max_ is None:
    print("UNSATISFIABLE")
else:
    print(min_, max_)
