n = int(input())
s = list(input())
q = int(input())

s1 = s[:n]
s2 = s[n:]

for i in range(q):
    t, a, b = list(map(int, input().split()))
    if t == 1:
        if a - 1 < n:
            temp = s1[a-1]
        else:
            temp = s2[a-1-n]

        if b - 1 < n:
            if a - 1 < n:
                s1[a-1] = s1[b-1]
            else:
                s2[a-1-n] = s1[b-1]
        else:
            if a - 1 < n:
                s1[a-1] = s2[b-1-n]
            else:
                s2[a-1-n] = s2[b-1-n]

        if b - 1 < n:
            s1[b-1] = temp
        else:
            s2[b-1-n] = temp

    elif t == 2:
        temp = s1
        s1 = s2
        s2 = temp

print("".join(s1+s2))