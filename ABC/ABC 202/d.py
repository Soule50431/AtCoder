a, b, k = map(int, input().split())
k -= 1
s = a + b
ans = []
bits = 0

shift = k // b
change = k % b
for i in range(b):
    bits += 1 << (i+1)

print(bits)
print(shift, change)
while change:

    change -= 1
for i in reversed(range(s)):
    if (bits>>i) & 1 == 0:
        ans.append("a")
    else:
        ans.append("b")

print(ans)