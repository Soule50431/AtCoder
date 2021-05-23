n = int(input())
a = list(map(int, input().split()))

max_list = [0] * n
max_list[0] = a[0]

for i in range(1, n):
    max_list[i] = max(max_list[i-1], a[i])
# print(max_list)

for i in range(1, n):
    a[i] += a[i-1]

for i in range(1, n):
    a[i] += a[i-1]

for i in range(n):
    print(max_list[i] * (i+1) + a[i])
