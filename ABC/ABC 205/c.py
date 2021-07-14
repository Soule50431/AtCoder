a, b, c = map(int, input().split())


if a >= 0 and b >= 0:
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("=")

if a < 0 and b >= 0:
    if abs(a) > b:
        if c % 2 == 0:
            print(">")
        else:
            print("<")
    elif abs(a) < b:
        print("<")
    else:
        if c % 2 == 0:
            print("=")
        else:
            print("<")

if a >= 0 and b < 0:
    if a > abs(b):
        print(">")

    elif a < abs(b):
        if c % 2 == 0:
            print("<")
        else:
            print(">")
    else:
        if c % 2 == 0:
            print("=")
        else:
            print(">")

if a < 0 and b < 0:
    if c % 2 == 0:
        if abs(a) > abs(b):
            print(">")
        elif abs(a) < abs(b):
            print("<")
        else:
            print("=")
    else:
        if abs(a) > abs(b):
            print("<")
        elif abs(a) < abs(b):
            print(">")
        else:
            print("=")


# temp = c
# ac = 1
# i = 1
# while c:
#     print(ac)
#     if c & 1 == 1:
#         ac *= a ** i
#     c >>= 1
#     i <<= 1
#
# bc = 1
# c = temp
# i = 1
# while c:
#     if c & 1 == 1:
#         bc *= b ** i
#     c >>= 1
#     i <<= 1
# # print(ac, bc)
# if ac > bc:
#     print(">")
# elif ac < bc:
#     print("<")
# else:
#     print("=")