s = input()

t = ""
len_s = len(s)
pointer = 0

while pointer < len_s:
    if s[pointer] == "e":
        if s[pointer:pointer+6] == "eraser":
            t += "eraser"
            pointer += 6
        elif s[pointer:pointer+5] == "erase":
            t += "erase"
            pointer += 5
        else:
            print("NO")
            exit()
    elif s[pointer] == "d":
        if s[pointer:pointer+11] == "dreameraser":
            t += "dreameraser"
            pointer += 11
        elif s[pointer:pointer+10] == "dreamerase":
            t += "dreamerase"
            pointer += 10
        elif s[pointer:pointer+7] == "dreamer":
            t += "dreamer"
            pointer += 7
        elif s[pointer:pointer+5] == "dream":
            t += "dream"
            pointer += 5
        else:
            print("NO")
            exit()
    else:
        print("NO")
        exit()

print("YES")
