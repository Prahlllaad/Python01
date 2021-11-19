n = int(input("Enter a Number: "))
sum = 1
i = 2
while n >= i * i:
    if n % i == 0:
        sum += i + (n / i)
    i += 1
if n != 1 and sum == n:
    print("Number is a Perfect Number. ")
else:
    print("Number is not a Perfect Number. ")