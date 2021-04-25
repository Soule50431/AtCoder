x = int(input())

five_hundred = x // 500
five = (x-500 * five_hundred) // 5

print(five*5 + five_hundred*1000)