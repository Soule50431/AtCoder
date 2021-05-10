s = list(input())

now = s[-1]
s.pop()
count = 0
for char in s[::-1]:
    if char != now:
        count += 1
        now = char
print(count)