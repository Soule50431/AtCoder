n, m, q = map(int, input().split())

baggage = []

for i in range(n):
    w, v = map(int, input().split())
    baggage.append([w, v])

boxes = list(map(int, input().split()))
# print(baggage)
# print(boxs)


def check(l, r):
    value = 0
    sorted_baggage = sorted(baggage, key=lambda x:x[1], reverse=True)
    # print(sorted_baggage)
    for i, box in enumerate(sorted(boxes[:l-1]+boxes[r:])):
        candidates = []
        for i, bag in enumerate(sorted_baggage):
            w, v = bag
            if box >= w:
                candidates.append([i, w, v])
        if candidates:
            candidates.sort(key=lambda x:x[2])
            value += candidates[-1][2]
            sorted_baggage.pop(candidates[-1][0])
    return value


for i in range(q):
    l, r = map(int, input().split())
    print(check(l, r))