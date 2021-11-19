n = int(input("Enter a Number: "))
sum = 0
while n > 0:
    sum += int(n % 10)
    n //= 10
print("Digital Sum = ", sum)