a, b = map(int, input().split())

remain = 16 - 2 * min(a, b)
left = abs(a - b)

if remain // 2 >= left:
    print("Yay!")
else:
    print(":(")
