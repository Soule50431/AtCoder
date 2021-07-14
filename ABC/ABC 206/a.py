import math

n = int(input())

if math.floor(1.08 * n) < 206:
    print("Yay!")
elif math.floor(1.08 * n) == 206:
    print("so-so")
else:
    print(":(")