n, m, q = map(int, input().split())

baggage = []

for i in range(n):
    w, v = map(int, input().split())
    baggage.append([i, w, v])

boxs = list(map(int, input().split()))
# print(baggage)
# print(boxs)


def check(l, r):
    dont_use = set(range(l-1,r))
    count = 0
    for bag in sorted(baggage, key=lambda x:x[2], reverse=True):
        for i, box in enumerate(sorted(boxs)):
            # print(i, box, bag)
            # print("II", dont_use)
            if box >= bag[1] and i not in dont_use:
                # print("ii")
                count += bag[2]
                dont_use.add(i)
                break

    return count


for i in range(q):
    l, r = map(int, input().split())
    print(check(l, r))