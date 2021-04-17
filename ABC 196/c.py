# n = input()
#
# count = 0
#
# for digit in range(1,len(n),2):
#     half = int((digit+1)/2)
#
#     for number in range(10**digit, min(10**(digit+1), int(n)+1)):
#         if str(number)[:half] == str(number)[half:]:
#             count += 1
#         # print(str(number)[:half], str(number)[half:])
#
# print(count)

################

n = int(input())
count = 0
i = 1

while True:
    if int(str(i) * 2) <= n:
        # print(int(str(i) * 2))
        count += 1
        i +=1
    else:
        break

print(count)