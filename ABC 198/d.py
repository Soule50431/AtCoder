# from collections import Counter
import itertools
# import sys
# input = sys.stdin.readline
#
# x = input().rstrip()
# y = input().rstrip()
# z = input().rstrip()
#
# # print(x, y, z)
# alphabets = list((Counter(x+y+z).keys()))
# digits = [str(i) for i in range(10)]
# if len(alphabets) > 10:
#     print("UNSOLVABLE")
# else:
#     # print(alphabets)
#     # print(digits)
#     for i in itertools.permutations(digits, len(alphabets)):
#         table = str.maketrans("".join(alphabets), "".join(i))
#
#         if table[ord(x[0])] == 48 or table[ord(y[0])] == 48 or table[ord(z[0])] == 48:
#             continue
#         else:
#             # print(x.translate(table), int(y.translate(table)), int(z.translate(table)))
#             if int(x.translate(table)) + int(y.translate(table)) == int(z.translate(table)):
#                 print(int(x.translate(table)))
#                 print(int(y.translate(table)))
#                 print(int(z.translate(table)))
#                 break
#     else:
#         print("UNSOLVABLE")

###############################
# u2dayo
S1 = input()[::-1]
S2 = input()[::-1]
S3 = input()[::-1]
print(S1)
print(S2)
print(S3)
# 英小文字を0～25の数字に変換します
# 対応関係の管理に、dictではなくlistを使うと3倍ほど早くなるためです。
L1 = [ord(char) - ord("a") for char in S1]
L2 = [ord(char) - ord("a") for char in S2]
L3 = [ord(char) - ord("a") for char in S3]
print(L1)
print(L2)
print(L3)
chars = set()
chars.update(L1, L2, L3)
M = len(chars)
print(chars)
def assign():
    D = [-1] * 26
    # 文字と数字の対応関係のリストを作ります
    for char, num in zip(chars, per):
        D[char] = num

    h1, h2, h3 = L1[-1], L2[-1], L3[-1]
    if D[h1] == 0 or D[h2] == 0 or D[h3] == 0:
        # 一番上の桁が0になる割当はできません
        return False, D
    return True, D

for per in itertools.permutations(range(10), r=M):
    assign()