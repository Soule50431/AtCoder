n, k = input().split()

x = n
for i in range(int(k)):
    g1 = int("".join(sorted(list(str(x)), reverse=True)))
    g2 = int("".join(sorted(list(str(x)))))
    x = g1 - g2
    # print(g1, g2, x)
print(x)

