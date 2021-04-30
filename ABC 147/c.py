from itertools import product

n = int(input())

testimonies = []
for i in range(n):
    a = int(input())
    testimony = []

    for j in range(a):
        x, y = map(int, input().split())
        testimony.append([x-1, y])
    testimonies.append(testimony)
# print(testimonies)

max_ = 0

for comb in product([0, 1], repeat=n):
    for i, x in enumerate(comb):
        contradiction = False
        for testimony in testimonies[i]:
            # if x == 0:  # 嘘つき
            #     if comb[testimony[0]] == testimony[1]:
            #         contradiction = True
            #         break
            if x == 1:  # 正直
                if comb[testimony[0]] != testimony[1]:
                    contradiction = True
                    break
        if contradiction:
            break
    else:
        max_ = max(max_, sum(comb))
print(max_)