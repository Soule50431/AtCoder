a, b = list(map(str, input().split()))

sa = 0
sb = 0
for char in a:
    sa += int(char)

for char in b:
    sb += int(char)

print(max(sa, sb))