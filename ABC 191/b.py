n, x = list(map(int, input().split()))
a = list(map(int, input().split()))


def not_x(n):
    return not n == x


print(*list(filter(not_x, a)))
