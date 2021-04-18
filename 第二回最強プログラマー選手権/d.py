import itertools

n, p = map(int, input().split())

count = 0
for a in itertools.product(range(1,p), repeat=n):
    temp = a[0]
    for i in range(1,n):
        temp += a[i]
        if temp % p == 0:
            break
    else:
        # print(a)
        count +=1

print(count%(10**9 + 7))