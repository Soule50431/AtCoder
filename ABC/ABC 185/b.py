n, m, t = list(map(int, input().split()))

battery = n
a = [0]
b = [0]
for i in range(m):
    a_, b_ = list(map(int, input().split()))
    a.append(a_)
    b.append(b_)

for i in range(1, m+1):
    battery -= (a[i] - b[i-1])
    # print(battery)
    if battery <= 0:
        print("No")
        exit()
    battery = min(n, battery+b[i]-a[i])
    # print(battery)

battery -= (t - b[i])
# print(battery)
if battery <= 0:
    print("No")
else:
    print("Yes")