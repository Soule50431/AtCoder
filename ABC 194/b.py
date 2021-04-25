import numpy as np

N = int(input())

A = []
B = []

for _ in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)

a_star, b_star = np.argmin(A), np.argmin(B)


if a_star == b_star:
    a, b = A[a_star], B[b_star]
    A[a_star] = np.inf
    B[b_star] = np.inf

    a_star, b_star = np.argmin(A), np.argmin(B)
    print(min(max(a, B[b_star]), max(A[a_star], b), a + b))

else:
    print(max(A[a_star], B[b_star]))