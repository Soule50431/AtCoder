import itertools

n = int(input())
l = list(map(int, input().split()))

count = 0
if n < 3:
    print(count)
    exit()

for comb in itertools.combinations(range(n),3):
    l1, l2, l3 = l[comb[0]], l[comb[1]], l[comb[2]]

    if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2 and l1 != l2 and l2 != l3 and l3 != l1:
        # print("i:", comb[0]+1, comb[1]+1, comb[2]+1)
        # print(l1, l2,l3)
        count += 1
print(count)