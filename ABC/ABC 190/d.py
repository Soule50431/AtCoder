n = int(input())

ans = 0

i = 1
while i**2 <= 2 * n:
    if 2 * n % i == 0:
        j = 2 * n // i
        if i % 2 != j % 2:
            ans += 2
            # print(i, j)
    i += 1
print(ans)
