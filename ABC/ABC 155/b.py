n = int(input())
a = list(map(int, input().split()))


for aa in a:
    if aa % 2 == 0:
        if not (aa % 3 == 0 or aa % 5 == 0):
            print("DENIED")
            exit()
print("APPROVED ")
