n, m, k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

a, b = [0], [0]

for i in range(n):
    a.append(a[i] + A[i])

for j in range(m):
    b.append(b[j] + B[j])

j_best = m+1
max_ = 0
# print(a, b)
for i in range(n+1):
    for j in reversed(range(j_best)):
        remain = k - a[i]
        if remain < 0:
            break
        # print(i, j, remain, b[j])
        if remain >= b[j]:
            # print("break")
            max_ = max(i + j, max_)
            j_best = j + 1
            break

print(max_)