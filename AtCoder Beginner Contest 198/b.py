n = str(input())

count = 0
for i in range(len(n)-1, -1, -1):
    if n[i] == "0":
        count += 1
    else:
        break

n = "0" * count + n

i = len(n) // 2
if len(n) % 2 == 0:
    # print(n[i - 1::-1], n[i:])
    if n[i-1::-1] == n[i:]:
        print("Yes")
    else:
        print("No")
else:
    # print(n[i::-1], n[i:])
    if n[i::-1] == n[i:]:
        print("Yes")
    else:
        print("No")