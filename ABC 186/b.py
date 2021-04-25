import numpy as np
h, w = list(map(int, input().split()))

a = []
for _ in range(h):
    a.append(list(map(int, input().split())))

print(np.sum(a-np.min(a)))
