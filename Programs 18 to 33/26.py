n1 = int(input("Enter a Number: "))
n2 = n1
sum = rem = 0
fact = 1
while n2 > 0:
    rem = n2 % 10
    for i in range(2, rem + 1):
        fact *= i
    sum += fact
    n2 //= 10
    fact = 1
if sum == n1:
    print("Number is a Strong number. ")
else:
    print("Number is not an Strong number. ")