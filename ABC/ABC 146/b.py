n = int(input())
s = list(input())

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 2

for char in s:
    print(alphabets[ord(char)-ord("A") + n], end="")
print()
