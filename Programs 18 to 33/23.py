n1 = int(input("Enter a Number: "))
n2 = n1
rem = rev = 0
while n2 > 0:
    rem = n2 % 10
    rev = (rev * 10) + rem
    n2 //= 10
if rev == n1:
    print("Number is a palindrome. ")
else:
    print("Number is not a palindrome. ")