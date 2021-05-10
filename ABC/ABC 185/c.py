l = int(input())

eleven_factorial = 39916800

sum_ = 1
for i in range(l-11, l):
    sum_ *= i
print(sum_ // eleven_factorial)