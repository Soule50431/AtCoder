from heapq import heapify, heappop, heappush
# 入力
n, m, q = map(int, input().split())

baggage = [list(map(int, input().split())) for i in range(n)]
# print(baggage)
boxes = list(map(int, input().split()))


def solve(l, r):
    use_boxes = boxes[:l] + boxes[r+1:]
    seen_bag = [False] * len(baggage)
    heap = []
    heapify(heap)
    ans = 0
    for box in sorted(use_boxes):
        for i, bag in enumerate(baggage):
            w, v = bag
            if box >= w and not seen_bag[i]:
                seen_bag[i] = True
                heappush(heap, -v)

        if heap:
            ans += - heappop(heap)
    return ans


for i in range(q):
    left, right = map(int, input().split())
    left -= 1
    right -= 1
    print(solve(left, right))

