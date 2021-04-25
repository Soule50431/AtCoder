import math

n = int(input())
a = list(map(int, input().split()))
# print(n)
# print(a)

temp = a[0]
sets = []
min = math.inf

for bit in range(1 << n):
    sets = []
    temp = a[0]
    # print(bin(bit))
    for j in range(1, n):
        if (bit >> (n - j - 1)) & 1:
            # print("a")
            sets.append(temp)
            temp = a[j]
        else:
            # print("b")
            temp |= a[j]
    sets.append(temp)
    #   print(sets)
    xor = sets[0]
    for l in sets[1:]:
        xor ^= l
    #   print(xor)
    if xor < min:
        min = xor

print(min)