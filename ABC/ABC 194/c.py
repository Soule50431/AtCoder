from collections import Counter

n = int(input())
a = list(map(int, input().split()))

counter = Counter(a)
# print(counter)
sum_ = 0
for i in range(-200, 200+1):
    for j in range(-200, 200+1):
        if i == j:
            continue
        # print(counter[i], counter[j])
        if (counter[i] != 0) and (counter[j] != 0):
            # print("comb", i, j)
            sum_ += counter[i] * counter[j] * abs(i-j) ** 2
print(int(sum_/2))