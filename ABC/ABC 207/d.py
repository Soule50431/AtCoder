import math
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
t = [list(map(int, input().split())) for _ in range(n)]


def rotate(x, y, theta):
    a = x + 1j * y
    b = a * (math.cos(theta) + 1j * math.sin(theta))
    return round(b.real), round(b.imag)


t_set = set([x + 1j * y for x, y in t])

for i in range(4):
    theta = i * math.pi / 2

    s_moved = [rotate(x, y, theta) for x, y in s]

    for j in range(n):
        for k in range(n):
            # print(si, tj)
            x_diff = t[k][0] - s_moved[j][0]
            y_diff = t[k][1] - s_moved[j][1]
            s_set = set([(x + x_diff) + 1j * (y + y_diff) for x, y in s_moved])
    #         s_set = set([x + 1j * y for x, y in s_moved])

            if len(s_set & t_set) == n:
                print("Yes")
                exit()
print("No")
