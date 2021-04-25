n = int(input())
a = list(map(int, input().split()))

product = 1

a = sorted(a)

if a[0] == 0:
    print(0)
    exit()

for i in a:
    product *= i
    if product > 10 ** 18:
        print(-1)
        exit()

print(product)