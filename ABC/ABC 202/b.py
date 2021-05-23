s = input()
ans = []
for char in reversed(s):
    if char == "6":
        ans.append("9")
    elif char == "9":
        ans.append("6")
    else:
        ans.append(char)
print("".join(ans))
