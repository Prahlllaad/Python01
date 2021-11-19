n = int(input("Enter Number of Terms: "))
sum = 0
temp = 3
for i in range(1, n + 1, 1):
    sum += temp
    temp = (temp * 10) + 3
print("Sum of Series = ", sum)