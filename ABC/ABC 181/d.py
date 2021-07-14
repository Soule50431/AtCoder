from collections import Counter
from itertools import product
s = list(input())
counter = Counter(s)

for comb in product(range(1, 10), repeat=min(3, len(s))):
    if int("".join(map(str, comb))) % 8 == 0:
        counter_temp = Counter(map(str, comb))
        for key in counter_temp:
            if counter[key] < counter_temp[key]:
                break
        else:
            print("Yes")
            exit()
print("No")

