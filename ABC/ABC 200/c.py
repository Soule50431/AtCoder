# import numpy as np
#
# n = int(input())
# a = np.array(list(map(int, input().split())))
#
# sum_ = 0
# for i in range(n):
#     # print((a - a[i]) % 200 == 0)
#     sum_ += sum((a - a[i]) % 200 == 0)
# print((sum_ - n) // 2)
from collections import Counter
n = int(input())
a = list(map(int, input().split()))

a = [i % 200 for i in a]

count = 0
counter = Counter(a)

for i in counter:
    num = counter[i]
    count += (num*(num-1)) // 2
print(count)