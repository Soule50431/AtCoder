import heapq

n = int(input())
a = list(map(int, input().split()))
a = list(map(lambda x: x*-1, a))
heapq.heapify(a)
alice = 0
bob = 0
while len(a) != 0:
    alice += heapq.heappop(a)*-1
    if len(a) != 0:
        bob += heapq.heappop(a) * -1
    else:
        break
print(alice - bob)




