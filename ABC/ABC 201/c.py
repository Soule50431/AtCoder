from itertools import combinations_with_replacement, permutations
s = input()

yes = set()
no = set()

for i, char in enumerate(s):
    if char == "o":
        yes.add(i)
    elif char == "x":
        no.add(i)

if len(yes) >= 5:
    print(0)
    exit()

length = len(yes)
digits = set(range(10))
remain = digits - no

all_ = set()
for comb in combinations_with_replacement(remain, r=4-length):
    temp = []
    for i in list(comb):
        temp.append(i)
    for i in list(yes):
        temp.append(i)

    for comb_ in permutations(temp):
        all_.add(comb_)
print(len(all_))


