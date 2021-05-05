import numpy as np
a = [list(map(int, input().split())) for i in range(3)]
a = np.array(a)
n = int(input())
b = []
bingo = np.zeros_like(a)

for i in range(n):
    b = int(input())
    index = np.where(a == b)
    if len(index[0]) != 0:
        bingo[index[0][0], index[1][0]] = 1

# チェック
if 3 in sum(bingo) or 3 in sum(bingo.T):
    print("Yes")
elif (bingo[0][0] and bingo[1][1] and bingo[2][2]) or (bingo[0][2] and bingo[1][1] and bingo[2][0]):
    print("Yes")
else:
    print("No")
