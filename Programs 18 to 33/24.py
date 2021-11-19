n1 = int(input("Enter a Number: "))
n2 = n1
sum = rem = 0
while n2 > 0:
    rem = n2 % 10
    sum += rem * rem * rem
    n2 //= 10
if sum == n1:
    print("Number is an Armstrong number. ")
else:
    print("Number is not an Armstrong number. ")