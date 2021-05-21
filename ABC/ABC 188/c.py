import numpy as np

n = int(input())
a = list(map(int, input().split()))

half = 2 ** (n-1)
left = np.argmax(a[:half])
right = np.argmax(a[half:])+half

if a[left] < a[right]:
    print(left+1)
else:
    print(right+1)