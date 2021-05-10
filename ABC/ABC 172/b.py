s = input()
t = input()

count = 0

for char_s, char_t in zip(s,t):
    if char_s != char_t:
        count += 1
print(count)