k = int(input())
a, b = map(int, input().split())

i = 1
while i * k <= b:
    if i * k >= a:
        print("OK")
        exit()
    i += 1
print("NG")