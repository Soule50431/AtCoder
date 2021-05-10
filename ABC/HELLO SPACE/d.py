from collections import deque

s = input()

t = deque()

reverse = False

for i in range(len(s)):
    if s[i] == "R":
        reverse = not reverse
    else:
        if reverse:
            if len(t) != 0:
                if t[0] == s[i]:
                    t.popleft()
                else:
                    t.appendleft(s[i])
            else:
                t.append(s[i])
        else:
            if len(t) != 0:
                if t[-1] == s[i]:
                    t.pop()
                else:
                    t.append(s[i])
            else:
                t.append(s[i])

ans = list(t)
if reverse:
    print("".join(ans[::-1]))
else:
    print("".join(ans))
