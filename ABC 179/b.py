n = int(input())

count = 0

for i in range(n):
    d1, d2 = list(map(int, input().split()))
    if d1 == d2:
        count += 1
    else:
        count = 0
    if count >= 3:
        print("Yes")
        exit()
print("No")