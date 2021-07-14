n = int(input())
a = list(map(int, input().split()))

for i, j in zip(sorted(a), range(1, n+1)):
    if i != j:
        print("No")
        exit()
print("Yes")