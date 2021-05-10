# s = input()
#
# max_ = -1
#
# count = 0
# for char in s:
#     if char == "S":
#         max_ = max(max_, count)
#         count = 0
#     else:
#         count += 1
#
# if s[2] == "R":
#     max_ = max(max_, count)
#
# print(max_)

s = input()

max_ = -1

count = 0
for char in s+"S":
    if char == "S":
        max_ = max(max_, count)
        count = 0
    else:
        count += 1

print(max_)