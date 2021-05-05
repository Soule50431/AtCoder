n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

output = list(a ^ b)

if len(output) == 0:
    pass
else:
    output = sorted(output)
    temp = [str(i) for i in output]
    print(" ".join(temp))