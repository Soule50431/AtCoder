x, y, z = map(int, input().split())
# print(x,y,z)

# if y % x == 0:
#     ans = int(y / x * z) - 1
# else:
#     ans = int(str(y / x * z).split(".")[0])
#
# if ans < 0:
#     print(0)
# else:
#     print(ans)

ans = (z*y) // x
if (z * y) % x == 0:
    ans -= 1

print(ans)