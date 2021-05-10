n, D, H = map(int, input().split())

max_ = 0

for i in range(n):
    d, h = map(int, input().split())
    y = H - ((H - h) / (D - d)) * D
    max_ = max(max_, y)
print(max_)

