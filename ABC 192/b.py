s = input()

for i, char in enumerate(s):
    if (i % 2 == 0 and (not char.islower())) or(i % 2 == 1 and (not char.isupper())):
        print("No")
        exit()

print("Yes")