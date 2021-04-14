from collections import Counter
import itertools
import sys
input = sys.stdin.readline

x = input().rstrip()
y = input().rstrip()
z = input().rstrip()

# print(x, y, z)
alphabets = list((Counter(x+y+z).keys()))
digits = [str(i) for i in range(10)]
if len(alphabets) > 10:
    print("UNSOLVABLE")
else:
    # print(alphabets)
    # print(digits)
    for i in itertools.permutations(digits, len(alphabets)):
        table = str.maketrans("".join(alphabets), "".join(i))

        if table[ord(x[0])] == 48 or table[ord(y[0])] == 48 or table[ord(z[0])] == 48:
            continue
        else:
            # print(x.translate(table), int(y.translate(table)), int(z.translate(table)))
            if int(x.translate(table)) + int(y.translate(table)) == int(z.translate(table)):
                print(int(x.translate(table)))
                print(int(y.translate(table)))
                print(int(z.translate(table)))
                break
    else:
        print("UNSOLVABLE")
