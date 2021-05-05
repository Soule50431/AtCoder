import numpy as np

n = int(input())
a = np.array(list(map(int, input().split())))

count  = 0
while all((a % 2) == 0):
    # print(a)
    a = a / 2
    count += 1
print(count)
