n = int(input())

count = 0
for i in range(1, n+1):
    decimal = set(list(str(i)))
    octal = set(oct(i))
    # print(i, decimal, octal)
    if "7" in decimal or "7" in octal:
        count += 1
print(n-count)
