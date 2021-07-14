n = int(input())
s = [input() for _ in range(n)]

t = 1
f = 0
for sn in reversed(s):
    t_temp = 0
    f_temp = 0
    if sn == "OR":
        t_temp += t * 2
        f_temp += t + f
    elif sn == "AND":
        t_temp += t + f
        f_temp += f * 2

    t = t_temp
    f = f_temp

print(t+f)