#series
#2*2+4*2+8*2+.....+n
n = int(input("Enter the position (n): "))
sum = 0
term = 2

for i in range(1, n + 1):
    sum += term ** 2
    term *= 2

print("The sum of the series till the nth position is:", sum)
