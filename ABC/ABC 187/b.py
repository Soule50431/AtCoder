n = int(input())

x = []
y = []

for _ in range(n):
    x_, y_ = list(map(int, input().split()))
    x.append(x_)
    y.append(y_)

count = 0

for i in range(n-1):
    for j in range(i+1, n):
        if -1 <= ((y[j] - y[i]) / (x[j] - x[i])) <= 1:
            count += 1
print(count)
