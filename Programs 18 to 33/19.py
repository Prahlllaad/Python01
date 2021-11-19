n = int(input("Enter a Number: "))
product = 1
while n > 0:
    product *= int(n % 10)
    n //= 10
print("Digital Product = ", product)