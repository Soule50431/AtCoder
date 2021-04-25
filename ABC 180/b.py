import numpy as np
n = int(input())
x = list(map(int, input().split()))

x = np.array(x)

print(np.sum(abs(x)))
print(np.sqrt(np.power(x,2).sum()))
print(max(abs(x)))