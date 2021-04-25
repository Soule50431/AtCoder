import math

n = int(input())
x_0 = list(map(int, input().split()))
x_n_2 = list(map(int, input().split()))

# print(n, x_0, x_n_2)
alpha = x_0[0] + x_0[1]*1j
x_opposite = x_n_2[0] + x_n_2[1] * 1j

# print(alpha)
# print(x_opposite)

theta = 2 * math.pi / n

rotate = math.cos(theta) + 1j * math.sin(theta)
# print(rotate)

beta = (x_opposite + alpha) / 2

y = rotate * (alpha - beta) + beta
print(y.real, y.imag)
